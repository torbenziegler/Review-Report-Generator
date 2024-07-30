from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.lib import colors

from pdf.utils.image_utils import download_image

class MyCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw_background(self):
        self.setFillColor(colors.lightgrey)
        self.rect(0, 0, letter[0], letter[1], fill=True)

def create_pdf(data, filename='Review_Report.pdf'):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Create a custom canvas and draw the background
    canvas = MyCanvas(filename, pagesize=letter)
    canvas.draw_background()
    canvas.save()

    # Create a document with the custom canvas
    doc = SimpleDocTemplate(filename, pagesize=letter)
    doc.build(elements, onFirstPage=lambda canvas, doc: MyCanvas(filename, pagesize=letter).draw_background())

    title = Paragraph("Review Report", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    create_pdf_metadata_section(elements, data, styles)

    if data:
        print("Creating Play Store Reviews section...")
        print(f"Total reviews: {len(data['comments'])}")
        elements.append(Paragraph("Play Store Reviews", styles['Heading1']))
        for review in data['comments']:
            print(f"Creating review: {review}")
            create_review(review, elements, styles)

    doc.build(elements)

def create_pdf_metadata_section(elements, playstore_reviews, styles):
    metadata = {
        "App Name": playstore_reviews['title'],
        "Description": playstore_reviews['description'],
        "Installs": playstore_reviews['installs'],
        "Real installs": playstore_reviews['realInstalls'],
        "free": playstore_reviews['free'],
        "inAppProductPrice": playstore_reviews['inAppProductPrice'],
        "developer": playstore_reviews['developer'],
        "developerEmail": playstore_reviews['developerEmail'], 
        "developerAddress": playstore_reviews['developerAddress'],
        "genre": playstore_reviews['genre'],
        "icon": playstore_reviews['icon'],
        "headerImage": playstore_reviews['headerImage'],
        "screenshots": playstore_reviews['screenshots'],
        "containsAds": playstore_reviews['containsAds'],
        "released": playstore_reviews['released'],
        "updated": playstore_reviews['updated'],
    }

    elements.append(Paragraph("Metadata", styles['Heading1']))
    for key, value in metadata.items():
        if key in ['icon', 'headerImage', 'screenshots']:
            if isinstance(value, list):  # For screenshots
                for image_url in value:
                    img = download_image(image_url)
                    if img:
                        elements.append(img)
            else:  # For single image URLs (Icon, Header Image)
                img = download_image(value)
                if img:
                    elements.append(img)
        else:
            elements.append(Paragraph(f"{key}: {value}", styles['Normal']))
    elements.append(Spacer(1, 12))

def create_review(review, elements, styles):
    comment = Paragraph(review, styles['Normal'])

    elements.append(comment)
    elements.append(Spacer(1, 12))