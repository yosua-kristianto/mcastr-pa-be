from core.model_integrator import EmoAnalyzerModel

def handle_text_analysis(text: str) -> str:
    """This handler function processes as bridge input text to perform sentiment analysis, 
    and take control of the logic to return the CDN URL of an image related to the sentiment of the text.

    The sentiment analysis logic is applied in the ML dedicated service layer.

    Args:
        text (str): The input text to analyze.

    Returns:
        str: The CDN URL of the image related to the sentiment of the text.
    """
    prediction = EmoAnalyzerModel().emo_analysis(text)
        
    match(prediction):
        case 0: return "Sadness"
        case 1: return "joy"
        case 2: return "love"
        case 3: return "anger"
        case 4: return "fear"
        case 5: return "suprise"
