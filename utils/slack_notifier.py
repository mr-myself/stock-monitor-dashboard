import requests
from datetime import datetime

class SlackNotifier:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_notification(self, trend_data):
        """Send notification to Slack"""
        color = "#00ff87" if trend_data['trend'] == 'uptrend' else "#ff4b4b"
        
        message = {
            "attachments": [
                {
                    "color": color,
                    "blocks": [
                        {
                            "type": "header",
                            "text": {
                                "type": "plain_text",
                                "text": f"NVIDIA Stock Trend Alert 🚨"
                            }
                        },
                        {
                            "type": "section",
                            "fields": [
                                {
                                    "type": "mrkdwn",
                                    "text": f"*Trend:* {trend_data['trend'].upper()}"
                                },
                                {
                                    "type": "mrkdwn",
                                    "text": f"*Current Price:* ${trend_data['current_price']:.2f}"
                                }
                            ]
                        },
                        {
                            "type": "section",
                            "fields": [
                                {
                                    "type": "mrkdwn",
                                    "text": f"*SMA20:* ${trend_data['sma20']:.2f}"
                                },
                                {
                                    "type": "mrkdwn",
                                    "text": f"*RSI:* {trend_data['rsi']:.2f}"
                                }
                            ]
                        },
                        {
                            "type": "context",
                            "elements": [
                                {
                                    "type": "mrkdwn",
                                    "text": f"Alert generated at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                                }
                            ]
                        }
                    ]
                }
            ]
        }
        
        try:
            response = requests.post(self.webhook_url, json=message)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error sending Slack notification: {e}")
            return False
