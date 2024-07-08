from transformers import pipeline

def analyze_driver_behavior(text):
    """Use a pre-trained language model to analyze driver behavior from text."""
    nlp = pipeline("sentiment-analysis")
    result = nlp(text)
    return result
