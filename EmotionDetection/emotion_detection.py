import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = input_json, headers = header)
    
    # If status code is 400, return None for all emotions
    if response.status_code == 400:
        return {key: None for key in ["anger", "disgust", "fear", "joy", "sadness", "dominant_emotion"]}
    
    else:
        response_dict = response.json()

        emotion = response_dict['emotionPredictions'][0]['emotion']

        max_value = 0
        for key in emotion.keys():
            if max_value < emotion[key]:
                max_value = emotion[key]
                max_key = key

        emotion['dominant_emotion'] = max_key

        return emotion