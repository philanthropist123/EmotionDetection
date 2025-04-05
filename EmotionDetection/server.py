from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
import json

app = Flask(__name__, template_folder='oaqjp-final-project-emb-ai/templates', static_folder='oaqjp-final-project-emb-ai/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST', 'GET'])
def emotionDetector():
    text_to_analyze = ""
    if request.method == 'POST':
        text_to_analyze = request.form['text']
    elif request.method == 'GET':
        text_to_analyze = request.args.get('textToAnalyze')

    if text_to_analyze:
        emotion_result = emotion_detector(text_to_analyze)

        if 'error' in emotion_result:
            return f"Error: {emotion_result['error']}"
        else:
            anger = emotion_result['anger']
            disgust = emotion_result['disgust']
            fear = emotion_result['fear']
            joy = emotion_result['joy']
            sadness = emotion_result['sadness']
            dominant_emotion = emotion_result['dominant_emotion']

            output_string = f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
            return output_string

    return "No text provided."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)