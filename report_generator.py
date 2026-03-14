from ai.prompt_engine import build_analysis_prompt

def generate_report(stock, fundamental, technical, news):

    prompt = build_analysis_prompt(stock, fundamental, technical, news)

    report = {
        "stock": stock,
        "analysis_prompt": prompt
    }

    return report