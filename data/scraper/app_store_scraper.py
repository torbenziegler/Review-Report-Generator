import requests
from bs4 import BeautifulSoup

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