from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from pdf.utils.image_utils import download_image
from pdf.utils.date_utils import format_date


def create_description_section(data, styles):
    img = download_image(data['icon'], (100, 100))

    description_text = f"{data['title']} is a {data['free'] is True and 'free' or 'paid'} app and was developed by {data['developer']} at {data['developerAddress']}."
    description_details = f"Released on {data['released']} and last updated on {format_date(data['updated'])}."
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