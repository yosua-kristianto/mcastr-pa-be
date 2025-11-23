import joblib
from pathlib import Path

from sklearn.svm import SVC
from sklearn.feature_extraction.text import HashingVectorizer
from lightgbm import LGBMClassifier

vectorizer = HashingVectorizer(
        ngram_range=(1, 3),   
        analyzer="word",
        alternate_sign=False, 
        n_features=2**18      
    )

class EmoAnalyzerModel:

    def __init__(self, choosen_model: str):
        self.choosen_model = choosen_model
        self.model = self.__model_loader()

    def __model_loader(self) -> SVC | LGBMClassifier:
        """
        @private
        Load the pre-trained SVC / LightGBM model from joblib file.
        Path: ../resources/model/model.joblib
        """
        model_path = Path(__file__).parent / f"../../resources/model/{self.choosen_model}-model.joblib"
        model = joblib.load(model_path.resolve())
        return model
    
    def emo_analysis(self, text: str) -> int:
        tensor = self.model.predict([text])
        prediction = tensor[0]

        print(f"Prediction: {prediction}")
        print(f"Tensor: {tensor}")

        return int(prediction)