from newsapi import NewsApiClient
import requests
import os
import json


API_KEY_NEWSAPI = os.environ.get("APIKey-NewsAPI")


def newsapi_client():
    # Using NewsApiClient object
    # ==========================

    # Init
    newsapi = NewsApiClient(api_key=API_KEY_NEWSAPI)

    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                              sources='bbc-news,the-verge',
                                              language='en')
    save_data_json(top_headlines, "top_headlines")

    # /v2/everything
    # TODO: Get current date and retrieve news from previous 2 days
    all_articles = newsapi.get_everything(q='tesla',
                                          from_param='2021-01-01',
                                          to='2021-01-07',
                                          language='en',
                                          sort_by='relevancy',
                                          page_size=3,
                                          page=1)
    save_data_json(all_articles, "everything")

    # /v2/sources
    sources = newsapi.get_sources(language="en")
    save_data_json(sources, "sources")


def newsapi_requests():
    # Using Python requests module
    # ============================

    base_url_newsapi = "https://newsapi.org/"

    endpoint_url_newsapi_top_headlines = "v2/top-headlines"
    endpoint_url_newsapi_everything = "v2/everything"
    endpoint_url_newsapi_sources = "v2/sources"

    url = base_url_newsapi + endpoint_url_newsapi_everything

    parameters_newsapi = {"api_key": API_KEY_NEWSAPI,
                          "q": 'tesla',
                          "from_param": '2021-01-01',
                          "to": '2021-01-07',
                          "language": 'en',
                          "sort_by": 'relevancy',
                          "page_size": 3,
                          "page": 1,
                          }

    response = requests.get(url=url, params=parameters_newsapi, timeout=1)
    response.raise_for_status()

    all_articles = response.json()
    save_data_json(all_articles, "sources")


def save_data_json(data, filename):
    # Save data to JSON file
    file_path = "./news/" + filename + ".json"
    with open(file_path, mode="w") as file:
        json.dump(data, fp=file)
