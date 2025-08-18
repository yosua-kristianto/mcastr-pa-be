import joblib
from pathlib import Path

from sklearn.svm import SVC
from sklearn.feature_extraction.text import HashingVectorizer

vectorizer = HashingVectorizer(
        ngram_range=(1, 3),   
        analyzer="word",
        alternate_sign=False, 
        n_features=2**18      
    )

class EmoAnalyzerModel:
    """
    EmoAnalyzerModel class to handle the loading of the pre-trained emotion analysis model.
    This class is responsible for integrating the model into the application.
    """

    def __init__(self):
        self.model = self.__model_loader()

    def __model_loader(self) -> SVC:
        """
        @private
        Load the pre-trained SVC model from joblib file.
        Path: ../resources/model/model.joblib
        """
        model_path = Path(__file__).parent / "../../resources/model/model.joblib"
        model = joblib.load(model_path.resolve())
        return model

    def emo_analysis(self, text: str) -> int:
        vector = vectorizer.transform([text])
        tensor = self.model.predict(vector)
        prediction = tensor[0]

        print(f"Prediction: {prediction}")
        print(f"Tensor: {tensor}")

        return int(prediction)
