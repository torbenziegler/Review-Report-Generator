from google_play_scraper import app, Sort, reviews


def fetch_playstore_data(package_name, lang='en'):
    result = app(
        package_name,
        lang=lang, # defaults to 'en'
        country='us' # defaults to 'us'
    )
    return result

def fetch_playstore_reviews(package_name, lang='en', count=5):
    result  = reviews(
        package_name,
        lang=lang, # defaults to 'en'
        country='us', # defaults to 'us'
        sort=Sort.NEWEST, # defaults to Sort.NEWEST
        count=100, # defaults to 100
        filter_score_with=5 # defaults to None(means all score)
    )
    return result[0] 