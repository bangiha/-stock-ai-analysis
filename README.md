from data.financials import get_financials
from data.price_data import get_price_data

ticker = "AAPL"

financials = get_financials(ticker)
price_data = get_price_data(ticker)

print(financials)
print(price_data.tail())
