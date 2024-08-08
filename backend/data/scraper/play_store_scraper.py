from google_play_scraper import app, Sort, reviews


def fetch_playstore_data(package_name, lang='en'):
    result = app(
        package_name,
        lang=lang,
        country='us' 
    )
    return result

def fetch_playstore_reviews(package_name, lang='en', count=100):
    result  = reviews(
        package_name,
        lang=lang, 
        country='us', 
        sort=Sort.NEWEST, 
        count=count, 
        filter_score_with=None # defaults to None(means all score)
    )
    return result[0] 