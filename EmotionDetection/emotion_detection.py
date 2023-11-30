import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url=url, headers=headers, json=obj)
    emotions = json.loads(response.text)['emotionPredictions'][0]['emotion']
    if response.status_code == 400:
        emotions['dominant_emotion'] = None
        for emotion, score in emotions.items():
            emotions[emotion] = None
        return emotions
    else:
        dominant = None
        dominant_score = 0
        for emotion, score in emotions.items():
            if score > dominant_score:
                dominant_score = score
                dominant = emotion
        emotions['dominant_emotion'] = dominant
        return emotions
