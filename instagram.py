import subprocess
from yt_dlp import YoutubeDL
from transcriber.whisper_transcriber import transcribe_stream


def get_direct_video_url(insta_url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'forceurl': True,
        'format': 'best[ext=mp4]',
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(insta_url, download=False)
            return info_dict['url']
    except Exception as e:
        print(f"[ERROR] Could not extract video URL: {e}")
        return None

def get_instagram_text(url):
    video_url = get_direct_video_url(url)
    if not video_url:
        return None
    return transcribe_stream(video_url)
