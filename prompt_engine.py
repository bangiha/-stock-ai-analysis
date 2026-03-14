def build_analysis_prompt(stock, fundamental, technical, news):

    prompt = f"""
    Analyze the following stock.

    Stock: {stock}

    Fundamental Data:
    {fundamental}

    Technical Data:
    {technical}

    News Sentiment:
    {news}

    Provide a full investment analysis including:
    - growth potential
    - risks
    - valuation
    - final investment opinion
    """

    return prompt