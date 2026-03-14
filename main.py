from data.financials import get_financials
from data.price_data import get_price_data
from analysis.fundamental import analyze_fundamentals
from analysis.technical import analyze_technical

ticker = "AAPL"

financials = get_financials(ticker)
price_data = get_price_data(ticker)

fundamental_result = analyze_fundamentals(financials)
technical_result = analyze_technical(price_data)

print("Fundamental Analysis")
print(fundamental_result)

print("Technical Analysis")
print(technical_result)