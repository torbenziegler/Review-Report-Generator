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

    create_pdf_title(elements, "Review Report", styles)
    create_pdf_metadata_section(elements, data, styles)
    create_pdf_image_section(elements, data)
    create_pdf_review_section(elements, data, styles)

    doc.build(elements)


def create_pdf_title(elements, title, styles):
    title = Paragraph(title, styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

def create_pdf_metadata_section(elements, data, styles):
    metadata = {
        "App Name": data['title'],
        "Description": data['description'],
        "Installs": data['installs'],
        "Real installs": data['realInstalls'],
        "free": data['free'],
        "inAppProductPrice": data['inAppProductPrice'],
        "developer": data['developer'],
        "developerEmail": data['developerEmail'], 
        "developerAddress": data['developerAddress'],
        "genre": data['genre'],
        "containsAds": data['containsAds'],
        "released": data['released'],
        "updated": data['updated'],
    }

    elements.append(Paragraph("Metadata", styles['Heading1']))
    for key, value in metadata.items():
        elements.append(Paragraph(f"{key}: {value}", styles['Normal']))

    

def create_pdf_image_section(elements, data):
    images = {
        "icon": data['icon'],
        "headerImage": data['headerImage'],
        "screenshots": data['screenshots'],
    }

    for key, value in images.items():
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
    elements.append(Spacer(1, 12))

def create_review(review, elements, styles):
    comment = Paragraph(review, styles['Normal'])

    elements.append(comment)
    elements.append(Spacer(1, 12))

def create_pdf_review_section(elements, data, styles):
    elements.append(Paragraph("Play Store Reviews", styles['Heading1']))
    for review in data['comments']:
        print(f"Creating review: {review}")
        create_review(review, elements, styles)