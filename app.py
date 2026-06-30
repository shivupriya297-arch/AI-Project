from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

lang_codes = {
    "Tamil": "ta",
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te"
}

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        text = request.form["text"]
        language = request.form["language"]

        result = GoogleTranslator(
            source="auto",
            target=lang_codes[language]
        ).translate(text)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)