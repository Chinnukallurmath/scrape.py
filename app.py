from fastapi import FastAPI, Query
from scrapers.instagram import get_instagram_text
from scrapers.reddit import get_reddit_text
from scrapers.linkdin import get_linkedin_text
from summarizer import summarize_text

app = FastAPI()

@app.get("/summarize")
def summarize(url: str):
    if "instagram.com" in url:
        text = get_instagram_text(url)
    elif "reddit.com" in url:
        text = get_reddit_text(url)
    elif "linkedin.com" in url:
        text = get_linkedin_text(url)
    else:
        return {"error": "Unsupported platform."}

    if not text:
        return {"error": "Failed to extract or transcribe content."}

    summary = summarize_text(text)
    return {"summary": summary}
