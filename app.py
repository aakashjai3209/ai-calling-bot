from flask import Flask, request, Response
from gtts import gTTS
import os
import uuid

app = Flask(__name__)

@app.route("/exotel", methods=["POST"])
def handle_call():
    user_input = request.form.get("SpeechResult", "Hello")

    ai_response = get_ai_response(user_input)
    audio_path = generate_audio(ai_response)

    response_xml = f"""
    <Response>
        <Play>{request.url_root}{audio_path}</Play>
    </Response>
    """

    return Response(response_xml, mimetype='text/xml')


def get_ai_response(text):
    return f"You asked: {text}. Here’s the answer..."

def generate_audio(text):
    tts = gTTS(text)
    filename = f"static/{uuid.uuid4()}.mp3"
    tts.save(filename)
    return filename

if __name__ == "__main__":
    if not os.path.exists("static"):
        os.mkdir("static")
    app.run(debug=True)
