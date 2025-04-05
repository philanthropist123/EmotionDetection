"""
Flask server for emotion detection application.
This module provides an API endpoint to analyze text and detect emotions.
"""
from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__, template_folder='oaqjp-final-project-emb-ai/templates',
            static_folder='oaqjp-final-project-emb-ai/static')

@app.route('/emotionDetector', methods=['POST', 'GET'])
def emotion_detector_api():
    """
    API endpoint that detects emotions in provided text.
    Accepts both GET and POST requests with text to analyze.
    Returns the emotion analysis results as a formatted string.
    """
    text_to_analyze = ""
    if request.method == 'POST':
        text_to_analyze = request.form['text']
    elif request.method == 'GET':
        text_to_analyze = request.args.get('textToAnalyze')

    emotion_result = emotion_detector(text_to_analyze)

    if isinstance(emotion_result, dict) and emotion_result.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"
    if 'error' in emotion_result:
        return f"Error: {emotion_result['error']}"

    # Extract emotions from result
    anger = emotion_result['anger']
    disgust = emotion_result['disgust']
    fear = emotion_result['fear']
    joy = emotion_result['joy']
    sadness = emotion_result['sadness']
    dominant_emotion = emotion_result['dominant_emotion']

    # Format output string across multiple lines for readability
    output_string = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    return output_string


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
