import requests
import json

def emotion_detector(text_to_analyze):

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        response_dict = json.loads(response.text)

        # Note the content formatting in this dictionary
        emotion_predictions = response_dict.get("emotionPredictions", [])
        if not emotion_predictions:
            return {"error": "No emotion data found"}

        emotions = emotion_predictions[0].get("emotion", {})
        anger_score = emotions.get("anger", 0.0)
        disgust_score = emotions.get("disgust", 0.0)
        fear_score = emotions.get("fear", 0.0)
        joy_score = emotions.get("joy", 0.0)
        sadness_score = emotions.get("sadness", 0.0)

        dominant_emotion = max(emotions, key=emotions.get, default="none")

        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    else:
        return {"error": f"Request failed with status code {response.status_code}", "details": response.text}