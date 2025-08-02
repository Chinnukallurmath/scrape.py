import whisper
import subprocess

model = whisper.load_model("base")

def transcribe_stream(video_url):
    print("🔁 Streaming and transcribing from URL...")

    command = [
        "ffmpeg",
        "-i", video_url,
        "-f", "wav",
        "-ar", "16000",
        "-ac", "1",
        "-loglevel", "quiet",
        "-"
    ]

    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        result = model.transcribe(process.stdout)
        return result["text"]
    except Exception as e:
        print(f"[ERROR] Transcription failed: {e}")
        return None
