from io import BytesIO
import requests
from PIL import Image
from reportlab.platypus import Image as RLImage

def download_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"Downloading image: {url}")
        image = Image.open(BytesIO(response.content))
        img_buffer = BytesIO()
        image.save(img_buffer, format='PNG')
        img_buffer.seek(0)
        print(f"Downloaded image: {url}")
        return RLImage(img_buffer)
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
        return None
    except Exception as e:
        print(f"Error processing image: {e}")
        return None
    