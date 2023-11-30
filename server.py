"""
This is a program to analyze text for emotions
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector as ed

app = Flask('Emotion Detection App')

@app.route("/")
def render_index_page():
    """
    This is to render a home page template
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def detect_emotion():
    """
    This is to analyze text for emotions
    """
    text_to_analyze = request.args['textToAnalyze']
    if not text_to_analyze:
        return 'Invalid text! Please try again!'
    emotions = ed(text_to_analyze)
    answer = 'For the given statement, the system response is '
    i = 0
    dominant = None
    for emotion, score in emotions.items():
        if emotion == 'dominant_emotion':
            dominant = score
            continue
        if i == len(emotions)-2 and i != 0:
            answer += f'and "{emotion}": {score}. '
        else:
            answer += f'"{emotion}": {score}, '
        i += 1
    answer += f'The dominant emotion is {dominant}.'
    return answer, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
