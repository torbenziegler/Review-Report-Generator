from datetime import datetime

def format_date(timestamp: str) -> str:
    """
    Convert a Unix timestamp to a human-readable date format.
    """
    return datetime.fromtimestamp(timestamp).strftime('%b %d, %Y')
