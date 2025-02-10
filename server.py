"""
Flask server for emotion detection application.

This module implements a web server that provides emotion detection services
through a REST API interface. It uses the EmotionDetection package to analyze
text and identify emotions.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


APP = Flask("EmotionDetector")


@APP.route("/emotionDetector", methods=["GET"])
def get_emotion():
    """Process emotion detection requests.

    This endpoint accepts text input via GET request and returns
    the emotion analysis results.

    Returns:
        str: Analysis results or error message
    """
    text = request.args.get('textToAnalyze', '')
    emotions = emotion_detector(text)

    if emotions['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return format_emotion_response(emotions)


def format_emotion_response(emotions):
    """Create formatted response string from emotion data.

    Args:
        emotions: Dict containing emotion scores and dominant emotion

    Returns:
        str: Formatted response string
    """
    return (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']:.9f}, "
        f"'disgust': {emotions['disgust']:.9f}, "
        f"'fear': {emotions['fear']:.9f}, "
        f"'joy': {emotions['joy']:.9f} and "
        f"'sadness': {emotions['sadness']:.9f}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )


@APP.route("/")
def render_index():
    """Serve the main page.

    Returns:
        str: Rendered index.html template
    """
    return render_template('index.html')


if __name__ == "__main__":
    APP.run(host='localhost', port=5000)
