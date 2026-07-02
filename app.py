import asyncio
import edge_tts

from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

lang_codes = {
    "Tamil": "ta",
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Japanese": "ja",
    "Korean": "ko",
    "Malayalam":"ml"
}

voice_codes = {
    "Tamil": "ta-IN-PallaviNeural",
    "English": "en-US-AriaNeural",
    "Hindi": "hi-IN-SwaraNeural",
    "Telugu": "te-IN-ShrutiNeural",
    "Japanese": "ja-JP-NanamiNeural",
    "Korean": "ko-KR-SunHiNeural",
    "Malayalam": "ml-IN-SobhanaNeural"
}

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        text = request.form.get("text", "")
        language = request.form.get("language", "English")

        if text.strip():
            result = GoogleTranslator(
                source="auto",
                target=lang_codes.get(language, "en")
            ).translate(text)

            voice = voice_codes.get(language, "en-US-AriaNeural")

            async def speak():
                communicate = edge_tts.Communicate(result, voice)
                await communicate.save("static/output.mp3")

            asyncio.run(speak())

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)