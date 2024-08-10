from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, ListFlowable, ListItem, Table
from data.chatgpt.summarize import summarize_text

def summarize_from_reviews(reviews):
    summary = summarize_text(reviews[:50])
    split_content = summary.split('\n- ')
    split_content = list(filter(None, split_content))
    return split_content


def build_user_feedback_section(reviews, styles):
    feedback = summarize_from_reviews(reviews)

    bullets = ListFlowable(
        [ListItem(Paragraph(text, styles['Normal']), bulletText='•') for text in feedback],
        bulletType='bullet'
    )

    title = Paragraph("User Feedback", styles['Heading2'])
    full_section = Table([
        [title],
        [bullets]
    ], colWidths=[letter[0]/2 - 6])

    return full_section

def build_tbd_section(styles):
    sample_text = [
        "Feedback point one for the right section.",
        "Feedback point two for the right section.",
        "Feedback point three for the right section."
    ]

    # Create a list flowable for the right section
    bullets = ListFlowable(
        [ListItem(Paragraph(text, styles['Normal']), bulletText='•') for text in sample_text],
        bulletType='bullet'
    )

    title = Paragraph("Section TBD", styles['Heading2'])
    full_section = Table([
        [title],
        [bullets]
    ], colWidths=[letter[0]/2 - 6])
    return full_section


def create_review_feedback_section(reviews, styles):
    return build_user_feedback_section(reviews, styles), build_tbd_section(styles)
