from reportlab.lib.units import inch

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