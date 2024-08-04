from reportlab.platypus import Paragraph, Spacer

def create_pdf_title(elements, title, styles):
    title_text = f"{title} Review Report"
    title = Paragraph(title_text, styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))