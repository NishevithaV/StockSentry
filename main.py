# StockSentry
#
# This script uses the Alpha Vantage API to retrieve daily time-series data for a specified equity symbol.
# The market summary is sent to user's phone as a notification using the Pushbullet API.

# Import necessary modules
import requests
import time
import pytz
from datetime import datetime
from pushbullet import Pushbullet

# API key for Pushbullet
PUSHB_API_KEY = 'PUSHBULLET_API_KEY'

# API key for Alpha Vantage
ALPHA_VANTAGE_API_KEY = 'ALPHAV_API_KEY'

# Equity symbol
EQUITY_SYMBOL = 'XXX'

# instance of Pushbullet
pb = Pushbullet(PUSHB_API_KEY)


# Obtains current day's market data
def getData():

    url = (
        f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY'
        f'&symbol={EQUITY_SYMBOL}&outputsize=full&apikey={ALPHA_VANTAGE_API_KEY}'
    )

    response = requests.get(url)

    if response.status_code == 200:
        alpha_vantage_data = response.json()

        if "Time Series (Daily)" in alpha_vantage_data:
            latest_date = list(alpha_vantage_data['Time Series (Daily)'].keys())[0]

            last_refreshed_date = datetime.strptime(latest_date, "%Y-%m-%d").date()

            current_datetime = datetime.now().date()

            if current_datetime == last_refreshed_date:

                data_today = alpha_vantage_data["Time Series (Daily)"][latest_date]
                open_price = data_today['1. open']
                high_price = data_today['2. high']
                low_price = data_today['3. low']
                close_price = data_today['4. close']
                volume = data_today['5. volume']

                return open_price, high_price, low_price, close_price, volume


# Only returns current day's market data if available at the end of trading hours
def marketOperational():

    # Current time in New York timezone
    ny_timezone = pytz.timezone('America/New_York')

    # Current time in New York
    currenttime_ny = datetime.now(ny_timezone)

    # allows for delay in data update in Alpha Vantage with an additional 30 minutes
    if currenttime_ny.hour >= 16 and currenttime_ny.minute >= 30:
        open_price, high_price, low_price, close_price, volume = getData()
        return open_price, high_price, low_price, close_price, volume


# Continuous loop to retrieve and send daily market data
while True:
    market_data = marketOperational()

    notification_title = f"Today's Market Summary for {EQUITY_SYMBOL} :"

    if market_data is not None:
        open_p, high_p, low_p, close_p, vol = market_data

        notification_body = (
            f"Opening price: ${open_p}\n"
            f"Today's high: ${high_p}\n"
            f"Today's low: ${low_p}\n"
            f"Closing price: ${close_p}\n"
            f"Volume traded: {vol}"
        )

    # no data to retrieve during weekends/ public holidays
    else:
        notification_body = "No market data to retrieve today."

    # send Pushbullet notification
    push = pb.push_note(notification_title, notification_body)

    # sleep for 24 hours before next iteration
    time.sleep(24*60*60)
