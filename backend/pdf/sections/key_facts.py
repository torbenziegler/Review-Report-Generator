from datetime import datetime
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from pdf.utils.date_utils import format_date

def create_key_facts_section(data, background_color=colors.lightgrey):
    app_name = f'<a href="{data["url"]}" color="blue">{data["title"]}</a>'
    app_name_paragraph = Paragraph(app_name, ParagraphStyle(name='Normal', textColor=colors.blue))
    score = data['score']
    if score is None:
        rating = "No Ratings"
    else:
        rating = str(round(score, 2))
    metadata = [
        ("Key Facts", ""),
        ("App Name", app_name_paragraph),
        ("Rating", rating),
        ("Installs", data['installs']),
        ("In-app Prices", data['inAppProductPrice'] or "None"),
        ("Contains Ads", data['containsAds']),
        ("Developer", data['developer']),
        ("Released", data['released']),
        ("Last Updated", format_date(data['updated'])),
    ]

    table = Table(metadata, colWidths=[80, 400])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), background_color),
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
