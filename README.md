# StockSentry



### Overview

StockSentry is a GitHub-based stock market program which leverages the Alpha Vantage and Pushbullet API to provide daily push notification updates on a chosen equity's performance. 


### Installation & Setup

All code is written in Python 3.9.0. The following are the required modules to be installed if you wish to clone the repository as seen in the requirements.txt:

```
requests == 2.31.0
pytz == 2023.3.post1
pushbullet.py == 0.12.0
```

### Usage & Adaptation

The following code snippet will be found in main.py:

```python
# API key for Pushbullet
PUSHB_API_KEY = 'PUSHBULLET_API_KEY'

# API key for Alpha Vantage
ALPHA_VANTAGE_API_KEY = 'ALPHAV_API_KEY'

# Equity symbol
EQUITY_SYMBOL = 'XXX'
```

To generate your unique API key for Pushbullet, visit [pushbullet.com](https://www.pushbullet.com/)

Similarly, you can obtain your API key for Alpha Vantage at [alphavantage.co](https://www.alphavantage.co/support/#api-key)

Once you have obtained your API keys, please replace the placeholder names 'PUSHBULLET_API_KEY' and 'ALPHAV_API_KEY' with yours. 

Finally, the equity symbol of the specific security for which you would like to receive daily updates will have to replace the placeholder 'XXX'. 

