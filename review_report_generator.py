from store_crawler import fetch_apple_reviews, fetch_playstore_reviews
from pdf_generator import create_pdf

if __name__ == "__main__":
    appstore_url = 'https://apps.apple.com/de/app/selfapy-mental-health-app/id1565142590?see-all=reviews'  # sample URL
    playstore_url = 'https://play.google.com/store/apps/details?id=com.selfapy.app'  # sample URL

    apple_reviews = fetch_apple_reviews(appstore_url)
    google_reviews = fetch_playstore_reviews(playstore_url)

    create_pdf(apple_reviews, google_reviews)
    print("PDF report created successfully!")
