import requests 
import json

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    myobj = {"raw_document": { "text": text_to_analyse } }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json = myobj, headers = headers)

def format_response(response):
    res = json.loads(response.text)
    formatted_output = res['EmotionPredictions'][0]['emotion']
    
    formatted_response = {
        'anger': formatted_output['anger'],
        'disgust': formatted_output['disgust'],
        'fear': formatted_output['fear'],
        'joy': formatted_output['joy'],
        'sadness': formatted_output['sadness'],
        'dominant_emotion': '<name of the dominant emotion>'
    }

    dominant_emotion = max(formatted_response, key = lambda x: formatted_response[x])
    formatted_response['dominant_dictionary'] = dominant_emotion
    return format_response

    