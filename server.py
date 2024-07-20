"""This is an emotional analyzer."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_function():
    """This function calls the emotion detector application."""
    text_to_analyze = request.args.get('text_to_analyze')
    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid Input! Please try again."

    response_text = (
        f"For the given statement, the system response is: "
        f"'anger': {response.get('anger', 'N/A')}, "
        f"'disgust': {response.get('disgust', 'N/A')}, "
        f"'fear': {response.get('fear', 'N/A')}, "
        f"'joy': {response.get('joy', 'N/A')}, "
        f"'sadness': {response.get('sadness', 'N/A')}. "
        f"The dominant emotion is {response.get('dominant_emotion', 'N/A')}."
    )
    return response_text


@app.route("/")
def render_index_page():
    ''' This is the function to render the html interface.'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
