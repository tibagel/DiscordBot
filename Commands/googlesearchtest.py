from googleapiclient.discovery import build
import pprint

my_api_key = "AIzaSyA3KQmf53-KmA_N1cd4RaZBqK1no_Jv8cM"
my_cse_id = "002146089033030040627:uemspje30hi"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search(
    'stackoverflow site:en.wikipedia.org', my_api_key, my_cse_id, num=10)
for result in results:
    pprint.pprint(result)

