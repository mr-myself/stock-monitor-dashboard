# Stock Monitor Dashboard

A real-time stock monitoring dashboard that provides interactive and engaging stock tracking with advanced technical analysis and notification capabilities.

## Features

- Real-time stock price monitoring (NVIDIA stock)
- Technical analysis indicators (SMA 12/26 days)
- RSI (Relative Strength Index) calculation
- Slack notifications for trend changes
- Interactive price charts with Plotly
- Mobile-responsive design

## Technical Stack

- Streamlit for web interface
- Python for data processing
- yfinance for real-time stock data
- Plotly for interactive charts
- Slack webhook integration

## Setup

1. Clone the repository
```bash
git clone https://github.com/mr-myself/stock-monitor-dashboard.git
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Set up environment variables
- `SLACK_WEBHOOK_URL`: Your Slack webhook URL for notifications

4. Run the application
```bash
streamlit run main.py
```

## License

This project is open-sourced under the MIT license.
