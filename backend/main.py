from pdf.pdf_generator import create_pdf
from data.chatgpt.summarize import summarize_text
from data.scraper.play_store_scraper import fetch_playstore_data, fetch_playstore_reviews

def generate_report(app_package_name):
    play_metadata = fetch_playstore_data(app_package_name)
    play_reviews = fetch_playstore_reviews(app_package_name)

    create_pdf(play_metadata, play_reviews)
    print("PDF report created successfully!")

if __name__ == "__main__":
    generate_report("com.google.android.apps.maps")