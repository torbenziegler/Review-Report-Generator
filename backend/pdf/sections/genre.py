from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

def create_genre_section(elements, data, styles, background_color=colors.lightgrey):
    category_label = "Genres" if len(data['categories']) > 1 else "Genre"
    metadata = [
        (category_label, "")
    ]
    metadata.extend([(genre['name'], "") for genre in data['categories']])

    # keep max 5 genres
    metadata = metadata[:5]
    table = Table(metadata, colWidths=[80, 80])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), background_color),
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