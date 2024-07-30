from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.lib import colors

class MyCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw_background(self):
        # Draw a background color
        self.setFillColor(colors.lightgrey)
        self.rect(0, 0, letter[0], letter[1], fill=True)

        # Optional: Draw an image as a background
        # self.drawImage('background_image.png', 0, 0, width=letter[0], height=letter[1])

def create_pdf(playstore_reviews, filename='Review_Report.pdf'):
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

    # TODO: Crawl metadata from the app store pages
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

    create_pdf_metadata_section(elements, metadata, styles)

    if playstore_reviews:
        elements.append(Paragraph("Play Store Reviews", styles['Heading1']))
        for review in playstore_reviews['comments']:
            create_review(review, elements, styles)

    doc.build(elements)

def create_pdf_metadata_section(elements, metadata, styles):
    elements.append(Paragraph("Metadata", styles['Heading1']))
    for key, value in metadata.items():
        elements.append(Paragraph(f"{key}: {value}", styles['Normal']))
    elements.append(Spacer(1, 12))

def create_review(review, elements, styles):
    review_title = Paragraph(f"Title: {review.get('title', 'No title')}", styles['Heading2'])
    review_rating = Paragraph(f"Rating: {review.get('rating', 'No rating')}", styles['Normal'])
    review_text = Paragraph(f"\"{review.get('text', 'No text')}\"", styles['Normal'])

    elements.append(review_title)
    elements.append(review_rating)
    elements.append(review_text)
    elements.append(Spacer(1, 12))

