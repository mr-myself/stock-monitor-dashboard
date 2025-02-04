import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import pandas as pd
from utils.stock_analyzer import StockAnalyzer
from utils.slack_notifier import SlackNotifier
import time

# Page configuration
st.set_page_config(
    page_title="NVIDIA Stock Monitor",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
with open('assets/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Initialize session state
if 'analyzer' not in st.session_state:
    st.session_state.analyzer = StockAnalyzer()
if 'slack_notifier' not in st.session_state:
    st.session_state.slack_notifier = SlackNotifier("YOUR_SLACK_WEBHOOK_URL")

# App title
st.markdown('<h1 class="stock-title">NVIDIA Stock Monitor</h1>', unsafe_allow_html=True)

# Create layout columns
col1, col2, col3 = st.columns(3)

def create_price_chart(data):
    """Create an interactive price chart with Plotly"""
    fig = go.Figure()
    
    # Candlestick chart
    fig.add_trace(go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name='OHLC'
    ))
    
    # Add moving averages
    fig.add_trace(go.Scatter(
        x=data.index,
        y=data['SMA20'],
        line=dict(color='yellow', width=1),
        name='SMA20'
    ))
    
    fig.add_trace(go.Scatter(
        x=data.index,
        y=data['SMA50'],
        line=dict(color='blue', width=1),
        name='SMA50'
    ))
    
    # Update layout
    fig.update_layout(
        template='plotly_dark',
        xaxis_rangeslider_visible=False,
        height=600,
        margin=dict(l=0, r=0, t=30, b=0)
    )
    
    return fig

def main():
    # Fetch and analyze real-time data
    data = st.session_state.analyzer.get_real_time_data()
    data = st.session_state.analyzer.calculate_technical_indicators(data)
    trend_data = st.session_state.analyzer.detect_trend(data)
    
    if trend_data:
        # Display metrics
        with col1:
            current_price = trend_data['current_price']
            st.metric(
                "Current Price",
                f"${current_price:.2f}",
                delta=f"{(current_price - data['Close'].iloc[-2]):.2f}"
            )

        with col2:
            st.metric(
                "Trend",
                trend_data['trend'].upper(),
                delta_color="normal"
            )

        with col3:
            st.metric(
                "RSI",
                f"{trend_data['rsi']:.2f}",
                delta=None
            )

        # Main chart
        st.plotly_chart(create_price_chart(data), use_container_width=True)

        # Send notification if needed
        if (trend_data['trend_changed'] and 
            trend_data['trend'] == 'uptrend' and 
            st.session_state.analyzer.should_notify()):
            st.session_state.slack_notifier.send_notification(trend_data)
            st.session_state.analyzer.last_notification_time = datetime.now()

        # Additional metrics
        col4, col5 = st.columns(2)
        
        with col4:
            st.markdown("### Technical Indicators")
            st.markdown(f"**SMA20:** ${trend_data['sma20']:.2f}")
            st.markdown(f"**SMA50:** ${trend_data['sma50']:.2f}")

        with col5:
            st.markdown("### Volume Analysis")
            st.markdown(f"**Daily Volume:** {data['Volume'].iloc[-1]:,.0f}")
            st.markdown(f"**Avg Volume:** {data['Volume'].rolling(20).mean().iloc[-1]:,.0f}")

if __name__ == "__main__":
    main()
    # Auto-refresh every minute
    time.sleep(60)
    st.experimental_rerun()
