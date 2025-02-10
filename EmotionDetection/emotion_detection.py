import requests

def emotion_detector(text_to_analyze):
    # API endpoint
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
        
    # Headers according to specification
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        }
        
    # Input JSON format as specified
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
        
    # Make POST request to the API
    response = requests.post(url, headers=headers, json=input_json)
    response_data = response.json()

    emotions = response_data['emotionPredictions'][0]['emotion']

    # Find the dominant emotion 
    dominant_emotion = max(emotions.items(), key=lambda x: x[1])[0]   
    emotions['dominant_emotion'] = dominant_emotion    

    return emotions
