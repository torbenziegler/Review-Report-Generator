import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def fetch_apple_reviews(url):
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

def fetch_playstore_reviews(url):
    response = requests.get(url)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all review containers
        review_containers = soup.find_all('div', class_='EGFGHd')

        reviews = []

        for container in review_containers:
            review = {}

            # Extract rating
            rating_element = container.find('div', class_='pf5lIe')
            if rating_element:
                rating = rating_element.find('div')['aria-label']
                review['rating'] = rating

            # Extract review title
            review_title_element = container.find('span', class_='X43Kjb')
            if review_title_element:
                review['title'] = review_title_element.text.strip()

            # Extract review text
            review_text_element = container.find('span', class_='jsname')
            if review_text_element:
                review['text'] = review_text_element.text.strip()

            reviews.append(review)
        
        return reviews
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []

def create_pdf(appstore_reviews, playstore_reviews, filename='Review_Report.pdf'):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    title = Paragraph("Review Report", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    # TODO: Crawl metadata from the app store pages
    metadata = {
        "App Name": "Selfapy",
        "Platform": "iOS & Android",
        "Date": "2021-08-20"
    }

    create_pdf_metadata_section(elements, metadata, styles)

    # TBD: Add Play Store reviews to the PDF report
    if playstore_reviews:
        pass

    if appstore_reviews:
        elements.append(Paragraph("App Store Reviews", styles['Heading1']))
        for review in appstore_reviews:
            create_review(review, elements, styles)

    doc.build(elements)

def create_pdf_metadata_section(elements, metadata, styles=getSampleStyleSheet()):
    elements.append(Paragraph("Metadata", styles['Heading1']))
    for key, value in metadata.items():
        elements.append(Paragraph(f"{key}: {value}", styles['Normal']))
    elements.append(Spacer(1, 12))

def create_review(review, elements, styles=getSampleStyleSheet()):
    review_title = Paragraph(f"Title: {review.get('title', 'No title')}", styles['Heading2'])
    review_rating = Paragraph(f"Rating: {review.get('rating', 'No rating')}", styles['Normal'])
    review_text = Paragraph(f"\"{review.get('text', 'No text')}\"", styles['Normal'])

    elements.append(review_title)
    elements.append(review_rating)
    elements.append(review_text)
    elements.append(Spacer(1, 12))

if __name__ == "__main__":
    appstore_url = 'https://apps.apple.com/de/app/selfapy-mental-health-app/id1565142590?see-all=reviews'  # sample URL
    playstore_url = 'https://play.google.com/store/apps/details?id=com.selfapy.app'  # sample URL

    apple_reviews = fetch_apple_reviews(appstore_url)
    google_reviews = fetch_playstore_reviews(playstore_url)

    # all_reviews = apple_reviews + playstore_reviews
    create_pdf(apple_reviews, google_reviews)
    print("PDF report created successfully!")
