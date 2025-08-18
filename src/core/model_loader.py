import requests
import time

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    print(response)
    return response.json()

def ner(text):
    while True:
        response = query({"inputs": text})

        if 'error' in response and 'loading' in response['error']:
            print(response['error'])
            time.sleep(10)  # Wait for 10 seconds before retrying
        else:
            return response

text = "Hugging Face Inc. is based in New York City."
print(ner(text))

# 
# import joblib
# import os

# model_directory = "../resources/sent-analysis/"

# labels = [
#     "anger", "disgust", "fear", "guilt", "humour",
#     "joy", "no_emotion", "sadness", "shame", "surprise"
# ]

# model = {}

# for label in labels:
#     model_path = os.path.join(model_directory, f"{label}.bin")
#     if os.path.exists(model_path):
#         model[label] = joblib.load(model_path)
#     else:
#         raise FileNotFoundError(f"Model file for label '{label}' not found at '{model_path}'")
    
# print("Model loaded successfully for labels:", list(model.keys()))