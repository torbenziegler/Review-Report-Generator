import os
from dotenv import load_dotenv

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from pdf.sections.report_title import create_pdf_title
from pdf.sections.key_facts import create_key_facts_section
from pdf.sections.description import create_description_section
from pdf.sections.performance import create_performance_section
from pdf.sections.review_feedback import create_review_feedback_section
from pdf.sections.genre import create_genre_section
from pdf.sections.footer import create_footer

load_dotenv()

IS_DEBUG = os.getenv('DEBUG_LAYOUT', 'False').lower() == 'true'

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


def create_layout(elements, data, reviews, styles):
    background_color = colors.lightgrey if IS_DEBUG is True else colors.white

    # First section with two columns (left and right)
    left_top = create_description_section(data, styles, background_color)

    left_bottom = create_performance_section(data)
    right_section = create_key_facts_section(data, background_color)
    
    table2 = Table([
        [left_top, right_section],
        [left_bottom, '']
    ], colWidths=[letter[0]/2 - 6, letter[0]/2 - 6])
    table2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), background_color),  # Background for left top cell
        ('BACKGROUND', (1, 0), (1, 0), background_color),  # Background for right section
        ('BACKGROUND', (0, 1), (0, 1), background_color),  # Background for left bottom cell
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
    
    table3 = Table([
        [left_section3, right_section3]
    ], colWidths=[letter[0]/2 - 6, letter[0]/2 - 6])
    table3.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), background_color),  # Background for left section
        ('BACKGROUND', (1, 0), (1, 0), background_color),  # Background for right section
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 10, colors.white)
    ]))
    elements.append(table3)
    elements.append(Spacer(1, 12))

    # Fourth section with three columns (left, middle, right)
    left_section4 = create_genre_section(elements, data, styles, background_color)
    middle_section4 = Paragraph("Sectors", styles['Normal'])
    # middle_section4 = Paragraph("Genres Chart", styles['Normal'])
    right_section4 = Paragraph("Some other chart 4", styles['Normal'])
    
    table4 = Table([
        [left_section4, middle_section4, right_section4]
    ], colWidths=[letter[0]/3 - 6, letter[0]/3 - 6, letter[0]/3 - 6])
    table4.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), background_color),  # Background for left section
        ('BACKGROUND', (1, 0), (1, 0), background_color),  # Background for middle section
        ('BACKGROUND', (2, 0), (2, 0), background_color),  # Background for right section
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 10, colors.white)
    ]))
    elements.append(table4)
    elements.append(Spacer(1, 12))