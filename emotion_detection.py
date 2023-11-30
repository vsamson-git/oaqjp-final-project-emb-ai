import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url=url, headers=headers, json=obj).text
    emotions = json.loads(response)['emotionPredictions'][0]['emotion']
    dominant = None
    dominant_score = 0
    print(emotions)
    for emotion, score in emotions:
        if score > dominant_score:
            dominant_score = score
            dominant = emotion
    emotions['dominant_emotion'] = emotion
    return emotions

print(emotion_detector('I love this new technology.'))