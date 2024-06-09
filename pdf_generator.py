from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(appstore_reviews, playstore_reviews, filename='Review_Report.pdf'):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    title = Paragraph("Review Report", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    # TODO: Crawl metadata from the app store pages
    metadata = {
        "App Name": "Selfapy",
        "Platform": "iOS & Android",
        "Date": "2021-08-20"
    }

    create_pdf_metadata_section(elements, metadata, styles)

    if appstore_reviews:
        elements.append(Paragraph("App Store Reviews", styles['Heading1']))
        for review in appstore_reviews:
            create_review(review, elements, styles)

    if playstore_reviews:
        elements.append(Paragraph("Play Store Reviews", styles['Heading1']))
        for review in playstore_reviews:
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
