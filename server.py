from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emo_det():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    
    # Check if dominant_emotion is None and return accordingly
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"  # Return 400 with custom error message
    else:
        # Generate a descriptive response from the dictionary
        formatted_response = (
            f"For the given statement, the system response is "
            f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, 'joy': {response['joy']} and "
            f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
        )
        
        return formatted_response, 200

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)