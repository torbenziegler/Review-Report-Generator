from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle , ListFlowable, ListItem, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from pdf.utils.image_utils import download_image
from pdf.utils.graph_utils import create_histogram_image
import matplotlib.pyplot as plt

class MyCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw_background(self):
        self.setFillColor(colors.lightgrey)
        self.rect(0, 0, letter[0], letter[1], fill=True)

def create_pdf(data, reviews, filename='Review_Report.pdf'):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    canvas = MyCanvas(filename, pagesize=letter)
    canvas.draw_background()
    canvas.save()

    doc = SimpleDocTemplate(filename, pagesize=letter)
    doc.build(elements, onFirstPage=add_page_decorations)

    create_pdf_title(elements, data['title'], styles)
    create_layout(elements, data, reviews, styles)
    
    doc.build(elements)

def add_page_decorations(canvas, doc):
    # Draw the background
    MyCanvas(canvas.getpdfdata(), pagesize=letter).draw_background()
    # Draw the footer
    create_footer(canvas, doc)

def create_pdf_title(elements, title, styles):
    title_text = f"{title} Review Report"
    title = Paragraph(title_text, styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

def create_key_facts_section(elements, data, styles):
    app_name = f'<a href="{data["url"]}" color="blue">{data["title"]}</a>'
    app_name_paragraph = Paragraph(app_name, ParagraphStyle(name='Normal', textColor=colors.blue))
    metadata = [
        ("Key Facts", ""),
        ("App Name", app_name_paragraph),
        ("Rating", str(round(data['score'], 2))),
        ("Installs", data['installs']),
        ("In-app Prices", data['inAppProductPrice'] or "None"),
        ("Contains Ads", data['containsAds']),
        ("Developer", data['developer']),
        ("Released", data['released']),
        ("Last Updated", datetime.fromtimestamp(data['updated']).strftime('%b %d, %Y')),
    ]

    table = Table(metadata, colWidths=[80, 400])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),  # Keys in bold
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    
    return table

def create_layout(elements, data, reviews, styles):
    # Second section with two columns (left and right)
    left_top = Paragraph("Description Section", styles['Normal'])
    left_top = create_description_section(elements, data, styles)

    left_bottom = create_performance_section(data)
    right_section = create_key_facts_section(elements, data, styles)
    
    table2 = Table([
        [left_top, right_section],
        [left_bottom, '']
    ], colWidths=[letter[0]/2 - 6, letter[0]/2 - 6])
    table2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), colors.lightgrey),  # Background for left top cell
        ('BACKGROUND', (1, 0), (1, 0), colors.lightgrey),  # Background for right section
        ('BACKGROUND', (0, 1), (0, 1), colors.lightgrey),  # Background for left bottom cell
        ('SPAN', (1, 0), (1, 1)),  # Right section spans two rows
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 10, colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    elements.append(table2)
    elements.append(Spacer(1, 12))

    # Third section with two columns (left and right)
    left_section3, right_section3 = create_review_feedback_section(elements, data, styles)
    #left_section3 = Paragraph("Left Section 3", styles['Normal'])
    # right_section3 = Paragraph("Right Section 3", styles['Normal'])
    
    table3 = Table([
        [left_section3, right_section3]
    ], colWidths=[letter[0]/2 - 6, letter[0]/2 - 6])
    table3.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), colors.lightgrey),  # Background for left section
        ('BACKGROUND', (1, 0), (1, 0), colors.lightgrey),  # Background for right section
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 10, colors.white)
    ]))
    elements.append(table3)
    elements.append(Spacer(1, 12))

    # Fourth section with three columns (left, middle, right)
    left_section4 = create_genre_section(elements, data, styles)
    middle_section4 = Paragraph("Sectors", styles['Normal'])
    # middle_section4 = Paragraph("Genres Chart", styles['Normal'])
    right_section4 = Paragraph("Some other chart 4", styles['Normal'])
    
    table4 = Table([
        [left_section4, middle_section4, right_section4]
    ], colWidths=[letter[0]/3 - 6, letter[0]/3 - 6, letter[0]/3 - 6])
    table4.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), colors.lightgrey),  # Background for left section
        ('BACKGROUND', (1, 0), (1, 0), colors.lightgrey),  # Background for middle section
        ('BACKGROUND', (2, 0), (2, 0), colors.lightgrey),  # Background for right section
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 10, colors.white)
    ]))
    elements.append(table4)
    elements.append(Spacer(1, 12))

def create_performance_section(data, img_size=(290, 180)):
    width, height = img_size
    histogram_image = create_histogram_image(data['histogram'], "Performance Histogram", "tbd x", "tbd y")
    performance_chart = Image(histogram_image, width, height)
    return performance_chart

def create_pdf_review_section(elements, reviews, styles):
    elements.append(Paragraph("Play Store Reviews", styles['Heading1']))
    for review in reviews:
        create_review(review, elements, styles)

def create_review(review, elements, styles):
    comment = Paragraph(review['content'], styles['Normal'])
    elements.append(comment)
    elements.append(Spacer(1, 12))


def create_description_section(elements, data, styles):
    # Download the image
    img = download_image(data['icon'], (100, 100))

    description_text = f"{data['title']} is a {data['free'] is True and 'free' or 'paid'} app and was developed by {data['developer']} at {data['developerAddress']}."
    description_details = f"Released on {data['released']} and last updated on {datetime.fromtimestamp(data['updated']).strftime('%b %d, %Y')}."
    full_description = f"{description_text} {description_details}"
    description = Paragraph(full_description, styles['Normal'])
    table_data = [[img, description]]
    
    # Create the table
    table = Table(table_data, colWidths=[1.5 * inch, 2.5 * inch])  # Adjust column widths as needed
    
    # Apply styles to the table
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (1, 0), (1, 0), 'Helvetica-Bold'),  # Only text in bold
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    
    return table


def create_review_feedback_section(elements, data, styles):
    # Sample text for the bullet point lists
    left_text = [
        "Feedback point one for the left section.",
        "Feedback point two for the left section.",
        "Feedback point three for the left section."
    ]
    
    right_text = [
        "Feedback point one for the right section.",
        "Feedback point two for the right section.",
        "Feedback point three for the right section."
    ]
    
    # Create a list flowable for the left section
    left_bullets = ListFlowable(
        [ListItem(Paragraph(text, styles['Normal']), bulletText='•') for text in left_text],
        bulletType='bullet'
    )
    
    # Create a list flowable for the right section
    right_bullets = ListFlowable(
        [ListItem(Paragraph(text, styles['Normal']), bulletText='•') for text in right_text],
        bulletType='bullet'
    )
    
    return left_bullets, right_bullets


def create_genre_section(elements, data, styles):
    category_label = "Genres" if len(data['categories']) > 1 else "Genre"
    metadata = [
        (category_label, "")
    ]
    metadata.extend([(genre['name'], "") for genre in data['categories']])

    # keep max 5 genres
    metadata = metadata[:5]
    table = Table(metadata, colWidths=[80, 80])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),  # Keys in bold
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    
    return table


def create_footer(canvas, doc):
    footer_text = 'This report was created by '
    footer_hyperlink = 'Review Report Generator'
    footer_url = 'https://github.com/torbenziegler/Review-Report-Scraper'
    
    # Set the footer text and add a hyperlink
    canvas.saveState()
    canvas.setFont('Helvetica', 9)
    
    # Position the footer at the bottom of the page
    text_width = canvas.stringWidth(footer_text, 'Helvetica', 9)
    hyperlink_width = canvas.stringWidth(footer_hyperlink, 'Helvetica-Bold', 9)
    
    x = (doc.pagesize[0] - text_width - hyperlink_width) / 2
    y = 0.5 * inch
    
    canvas.drawString(x, y, footer_text)
    x += text_width
    canvas.setFont('Helvetica-Bold', 9)
    canvas.drawString(x, y, footer_hyperlink)
    
    # Add the hyperlink annotation
    canvas.linkURL(footer_url, (x, y - 2, x + hyperlink_width, y + 10), relative=1)
    canvas.restoreState()
