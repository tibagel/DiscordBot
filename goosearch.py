from googleapiclient.discovery import build
from token_babo import my_api_key
from token_babo import my_cse_id


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

def q_google(search):
    results = google_search(search,my_api_key,my_cse_id,num=1)
    for result in results:
        return result['link']
