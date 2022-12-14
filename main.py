from flask import Flask, render_template
import requests

import yfinance as yf

# getting the current stock price of GME using yfinance API
def get_gme_price():
    stock_info = yf.Ticker('GME').info
    market_price = stock_info['regularMarketPrice']
    return market_price

app = Flask(__name__)

@app.route('/')
def index():
    gme_price = get_gme_price()
    return render_template("index.html", gme_price=gme_price)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

#app.run(host="0.0.0.0", port=8000)