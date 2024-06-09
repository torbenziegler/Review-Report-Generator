import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def fetch_reviews(url):
    response = requests.get(url)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all review containers
        review_containers = soup.find_all('div', class_='we-customer-review')

        reviews = []

        for container in review_containers:
            review = {}

            # Extract rating
            rating_element = container.find('figure', class_='we-star-rating we-customer-review__rating we-star-rating--large')
            if rating_element:
                rating = rating_element.get('aria-label')
                review['rating'] = rating

            # Extract review title
            review_title_element = container.find('h3', class_='we-customer-review__title')
            if review_title_element:
                review['title'] = review_title_element.text.strip()

            # Extract review text
            review_text_element = container.find('blockquote', class_='we-customer-review__body')
            if review_text_element:
                review['text'] = review_text_element.text.strip()

            reviews.append(review)
        
        return reviews
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []

def create_pdf(reviews, filename='Review_Report.pdf'):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    title = Paragraph("Review Report", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    for review in reviews:
        review_title = Paragraph(f"Title: {review.get('title', 'No title')}", styles['Heading2'])
        review_rating = Paragraph(f"Rating: {review.get('rating', 'No rating')}", styles['Normal'])
        review_text = Paragraph(f"Text: {review.get('text', 'No text')}", styles['Normal'])

        elements.append(review_title)
        elements.append(review_rating)
        elements.append(review_text)
        elements.append(Spacer(1, 12))

    doc.build(elements)

if __name__ == "__main__":
    URL = 'https://apps.apple.com/de/app/selfapy-mental-health-app/id1565142590?see-all=reviews'
    reviews = fetch_reviews(URL)
    create_pdf(reviews)
