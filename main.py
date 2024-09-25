from flask import Flask, request, jsonify
import whisper

app = Flask(__name__)
model = whisper.load_model("base")

@app.route("/transcribe", methods=["POST"])
def transcribe_audio():
    file = request.files["file"]
    file.save("temp.mp4")
    result = model.transcribe("temp.mp4",language = "pl")
    return jsonify({"transcription": result["text"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
