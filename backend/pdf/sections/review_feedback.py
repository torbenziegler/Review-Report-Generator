from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, ListFlowable, ListItem

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