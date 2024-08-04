from pdf.pdf_generator import create_pdf
from data.scraper.play_store_scraper import fetch_playstore_data, fetch_playstore_reviews

if __name__ == "__main__":
    app_package_name = 'com.whatsapp'  # sample package name
    play_metadata = fetch_playstore_data(app_package_name)
    play_reviews = fetch_playstore_reviews(app_package_name)

    create_pdf(play_metadata, play_reviews)
    print("PDF report created successfully!")
