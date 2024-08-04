from datetime import datetime

def format_date(timestamp: str) -> str:
    return datetime.fromtimestamp(timestamp).strftime('%b %d, %Y')