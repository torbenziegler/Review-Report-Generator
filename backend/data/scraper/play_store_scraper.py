from google_play_scraper import app, Sort, reviews


def fetch_playstore_data(package_name, lang='en'):
    """
    Fetches the metadata of the app with the given package name.
    """
    result = app(
        package_name,
        lang=lang,
        country='us'
    )
    return result

def fetch_playstore_reviews(package_name, lang='en', count=100):
    """
    Fetches the reviews of the app with the given package name.
    """
    result  = reviews(
        package_name,
        lang=lang,
        country='us',
        sort=Sort.NEWEST,
        count=count, 
        filter_score_with=None # defaults to None(means all score)
    )
    return result[0]
