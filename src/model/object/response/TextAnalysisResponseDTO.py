
class TextAnalysisResponseDTO:

    def __init__(self, image_uri: str = "", feedback_uri: str = ""):
        self.image_uri = image_uri
        self.feedback_id = feedback_uri
    