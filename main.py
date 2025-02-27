import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import pandas as pd
import os
from utils.stock_analyzer import StockAnalyzer
from utils.slack_notifier import SlackNotifier

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
    webhook_url = os.environ.get('SLACK_WEBHOOK_URL')
    st.session_state.slack_notifier = SlackNotifier(webhook_url) if webhook_url else None

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

    # Add moving averages if they exist
    if 'SMA12' in data.columns:  # Changed from SMA20
        fig.add_trace(go.Scatter(
            x=data.index,
            y=data['SMA12'],
            line=dict(color='yellow', width=1),
            name='SMA12'  # Changed from SMA20
        ))

    if 'SMA26' in data.columns:  # Changed from SMA50
        fig.add_trace(go.Scatter(
            x=data.index,
            y=data['SMA26'],
            line=dict(color='blue', width=1),
            name='SMA26'  # Changed from SMA50
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
    try:
        # Fetch and analyze real-time data
        data = st.session_state.analyzer.get_real_time_data()
        if not data.empty:
            data = st.session_state.analyzer.calculate_technical_indicators(data)
            trend_data = st.session_state.analyzer.detect_trend(data)

            if trend_data:
                # Display metrics
                with col1:
                    current_price = trend_data['current_price']
                    prev_close = data['Close'].iloc[-2] if len(data) > 1 else current_price
                    st.metric(
                        "Current Price",
                        f"${current_price:.2f}",
                        delta=f"{(current_price - prev_close):.2f}"
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

                # Send notification if needed (only if Slack is configured)
                if (st.session_state.slack_notifier and
                    trend_data['trend_changed'] and 
                    trend_data['trend'] == 'uptrend' and 
                    st.session_state.analyzer.should_notify()):
                    st.session_state.slack_notifier.send_notification(trend_data)
                    st.session_state.analyzer.last_notification_time = datetime.now()

                # Additional metrics
                col4, col5 = st.columns(2)

                with col4:
                    st.markdown("### Technical Indicators")
                    st.markdown(f"**SMA12:** ${trend_data['sma12']:.2f}")  # Changed from SMA20
                    st.markdown(f"**SMA26:** ${trend_data['sma26']:.2f}")  # Changed from SMA50

                with col5:
                    st.markdown("### Volume Analysis")
                    st.markdown(f"**Daily Volume:** {data['Volume'].iloc[-1]:,.0f}")
                    st.markdown(f"**Avg Volume:** {data['Volume'].rolling(20).mean().iloc[-1]:,.0f}")
        else:
            st.error("Unable to fetch stock data. Please check your connection.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
    st.empty()  # This will trigger a rerun every few seconds