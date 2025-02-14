import requests  # Import the requests library to handle HTTP requests
import json # Import json library to parse response text

def emotion_detector(text_to_analyse):  # Define a function named emotion_detector that takes a string input (text_to_analyse)
    # URL of the emotion predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    
    # Create payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } } 

    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  
    
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)

    # Handle error if text_to_analyse was incorrect
    if response.status_code == 400:
        emotion = {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion":None}
        return emotion

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting emotion scores from the response
    emotion = formatted_response["emotionPredictions"][0]["emotion"]

    # Highest score emotion is dominant emotion
    emotion["dominant_emotion"] = max(emotion, key=emotion.get)

    return emotion