import pandas as pd

def analyze_technical(price_data):

    price_data["MA50"] = price_data["Close"].rolling(window=50).mean()
    price_data["MA200"] = price_data["Close"].rolling(window=200).mean()

    latest = price_data.iloc[-1]

    signal = "Neutral"

    if latest["MA50"] > latest["MA200"]:
        signal = "Bullish"

    if latest["MA50"] < latest["MA200"]:
        signal = "Bearish"

    return {
        "technical_signal": signal
    }