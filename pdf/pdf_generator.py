from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics import renderPDF
from datetime import datetime

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

    # Create a custom canvas and draw the background
    canvas = MyCanvas(filename, pagesize=letter)
    canvas.draw_background()
    canvas.save()

    # Create a document with the custom canvas
    doc = SimpleDocTemplate(filename, pagesize=letter)
    doc.build(elements, onFirstPage=lambda canvas, doc: MyCanvas(filename, pagesize=letter).draw_background())

    create_pdf_title(elements, "Review Report", styles)
    create_layout(elements, data, styles)
    
    # create_pdf_review_section(elements, reviews, styles)

    doc.build(elements)

def create_pdf_title(elements, title, styles):
    title = Paragraph(title, styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

def create_pdf_metadata_section(elements, data, styles):
    metadata = [
        ("Key Facts", ""),
        ("App Name", data['title']),
        ("Rating", str(round(data['score'], 2))),
        ("Installs", data['installs']),
        ("In-app Prices", data['inAppProductPrice']),
        ("Developer", data['developer']),
        ("Released", data['released']),
        ("Last Updated", datetime.fromtimestamp(data['updated']).strftime('%Y-%m-%d')),
    ]

    table = Table(metadata, colWidths=[80, 400])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),  # Keys in bold
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    
    return table

def create_layout(elements, data, styles):
    # Second section with two columns (left and right)
    left_top = Paragraph("Description Section", styles['Normal'])
    left_bottom = Paragraph("Performance Chart Section", styles['Normal'])
    right_section = create_pdf_metadata_section(elements, data, styles)
    
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
        ('GRID', (0, 0), (-1, -1), 10, colors.white)
    ]))
    elements.append(table2)
    elements.append(Spacer(1, 12))

    # Third section with two columns (left and right)
    left_section3 = Paragraph("Left Section 3", styles['Normal'])
    right_section3 = Paragraph("Right Section 3", styles['Normal'])
    
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
    left_section4 = Paragraph("Sectors", styles['Normal'])
    # pull from data 'categories'
    middle_section4 = Paragraph("Genres Chart", styles['Normal'])
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

def create_pdf_review_section(elements, reviews, styles):
    elements.append(Paragraph("Play Store Reviews", styles['Heading1']))
    for review in reviews:
        create_review(review, elements, styles)

def create_review(review, elements, styles):
    comment = Paragraph(review['content'], styles['Normal'])
    elements.append(comment)
    elements.append(Spacer(1, 12))

def create_pie_chart(data, title="Pie Chart"):
    # Create a Drawing object
    drawing = Drawing(300, 200)
    
    # Create a Pie chart instance
    pie = Pie()
    
    # Set pie chart data
    pie.data = [data[key] for key in data]
    pie.labels = list(data.keys())
    
    # Set the position and size of the pie chart
    pie.x = 50
    pie.y = 50
    pie.width = 200
    pie.height = 150
    
    # Set colors for slices (optional)
    pie.slices.strokeColor = colors.black
    pie.slices.fillColor = [colors.red, colors.green, colors.blue, colors.yellow]

    # Add the pie chart to the drawing
    drawing.add(pie)

    # Return the Drawing object
    return drawing
