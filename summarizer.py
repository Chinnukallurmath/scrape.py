from transformers import pipeline

# Load transformer pipeline
summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_length=120):
    # Split long text into chunks of 1024 tokens
    chunks = [text[i:i+1024] for i in range(0, len(text), 1024)]

    # Generate summary for each chunk
    summaries = [
        summarizer_pipeline(chunk, max_length=max_length, min_length=30, do_sample=False)[0]['summary_text']
        for chunk in chunks
    ]

    return " ".join(summaries)
