import yfinance as yf

def get_financials(ticker):
    stock = yf.Ticker(ticker)

    data = {
        "revenue": stock.financials,
        "balance_sheet": stock.balance_sheet,
        "cashflow": stock.cashflow
    }

    return data