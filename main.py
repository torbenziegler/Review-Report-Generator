# from app_store_scraper import fetch_apple_reviews, fetch_playstore_reviews
from pdf.pdf_generator import create_pdf
from data.play_store_scraper import fetch_playstore_data

if __name__ == "__main__":
    playstore_url = 'https://play.google.com/store/apps/details?id=com.selfapy.app'  # sample URL
    google_reviews = fetch_playstore_data('com.nianticlabs.pokemongo')

    create_pdf(google_reviews)
    print("PDF report created successfully!")
