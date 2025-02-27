import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta

class StockAnalyzer:
    def __init__(self, symbol='NVDA', window_size=12):  # Changed from 20 to 12
        self.symbol = symbol
        self.window_size = window_size
        self.current_trend = None
        self.last_notification_time = None
        self.notification_cooldown = timedelta(minutes=30)

    def get_real_time_data(self):
        """Fetch real-time stock data"""
        stock = yf.Ticker(self.symbol)
        data = stock.history(period='1d', interval='1m')
        return data

    def get_historical_data(self, period='1mo'):
        """Fetch historical stock data"""
        stock = yf.Ticker(self.symbol)
        data = stock.history(period=period)
        return data

    def calculate_technical_indicators(self, data):
        """Calculate technical indicators for trend detection"""
        # Calculate moving averages with shorter periods for faster trend detection
        data['SMA12'] = data['Close'].rolling(window=12).mean()  # Changed from SMA20
        data['SMA26'] = data['Close'].rolling(window=26).mean()  # Changed from SMA50

        # Calculate RSI
        delta = data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        data['RSI'] = 100 - (100 / (1 + rs))

        return data

    def detect_trend(self, data):
        """Detect price trend using multiple indicators with shorter moving averages"""
        if len(data) < self.window_size:
            return None

        current_price = data['Close'].iloc[-1]
        sma12 = data['SMA12'].iloc[-1]  # Changed from sma20
        sma26 = data['SMA26'].iloc[-1]  # Changed from sma50
        rsi = data['RSI'].iloc[-1]

        # Define trend conditions
        uptrend_conditions = [
            current_price > sma12,  # Changed from sma20
            sma12 > sma26,         # Changed from sma20 > sma50
            rsi > 50
        ]

        downtrend_conditions = [
            current_price < sma12,  # Changed from sma20
            sma12 < sma26,         # Changed from sma20 < sma50
            rsi < 50
        ]

        if all(uptrend_conditions):
            new_trend = 'uptrend'
        elif all(downtrend_conditions):
            new_trend = 'downtrend'
        else:
            new_trend = 'neutral'

        # Check if trend has changed
        trend_changed = (self.current_trend != new_trend)
        self.current_trend = new_trend

        return {
            'trend': new_trend,
            'trend_changed': trend_changed,
            'current_price': current_price,
            'sma12': sma12,        # Changed from sma20
            'sma26': sma26,        # Changed from sma50
            'rsi': rsi
        }

    def should_notify(self):
        """Check if we should send a notification based on cooldown"""
        if not self.last_notification_time:
            return True

        time_since_last = datetime.now() - self.last_notification_time
        return time_since_last > self.notification_cooldown