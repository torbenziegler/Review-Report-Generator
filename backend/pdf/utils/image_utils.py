from io import BytesIO
import requests
from PIL import Image
from reportlab.platypus import Image as RLImage

def download_image(url, size=None):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print(f"Downloading image: {url}")
        image = Image.open(BytesIO(response.content))
        if size is not None:
            print(f"Resizing image to: {size}")
            image = image.resize(size, Image.LANCZOS)

        img_buffer = BytesIO()
        image.save(img_buffer, format='PNG')
        img_buffer.seek(0)
        return RLImage(img_buffer)
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
        return None
    except Exception as e:
        print(f"Error processing image: {e}")
        return None
