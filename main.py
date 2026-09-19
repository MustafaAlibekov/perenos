from flask import Flask, render_template, request
from transformers import pipeline
app = Flask(__name__)
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="blanchefort/rubert-base-cased-sentiment"
)
@app.route("/", methods=['GET', "POST"])
def index():
    user_text = ""
    recommendation = None
    if request.method == "POST":
        user_text = request.form.get('message', '')
        if user_text:
            result = sentiment_analyzer(user_text)[0]
            if result['label'] == 'POSITIVE':
                recommendation = "отлично, продолджай в том же духе."
            elif result['label'] == 'NEGATIVE':
                recommendation = "не расстраивайся, все наладится."
            else:
                recommendation = "спокойствие - тоже хорошо."
        return render_template('index.html', user_text=user_text, recommendation=recommendation)
        if __name__ == '__name__':
            app.run(debug=True)
