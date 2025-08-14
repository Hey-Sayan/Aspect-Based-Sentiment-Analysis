from flask import Flask, request, render_template
from textblob import TextBlob

app = Flask(__name__)

def get_sentiment(text):
    score = TextBlob(text).sentiment.polarity
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

@app.route('/', methods=['GET', 'POST'])
def home():
    sentiment = None
    text = ""
    if request.method == 'POST':
        text = request.form['review']
        sentiment = get_sentiment(text)
    return render_template('index.html', sentiment=sentiment, text=text)

if __name__ == '__main__':
    app.run(debug=True)
