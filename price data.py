import yfinance as yf

def get_price_data(ticker):
    stock = yf.Ticker(ticker)

    price_data = stock.history(period="1y")

    return price_data