from google_play_scraper import app


def fetch_playstore_data(package_name, lang='en'):
    result = app(
        package_name,
        lang=lang, # defaults to 'en'
        country='us' # defaults to 'us'
    )
    return result