from newsapi import NewsApiClient
import requests
import os
import save_data


API_KEY = os.environ.get("APIKey-NewsAPI")


def newsapi_client(stock, company):
    """
    Using NewsApiClient object -
    Note that NewsApiClient uses underscores in parameter names:
    exclude_domains, sort_by, page_size, api_key
    """

    # Init
    newsapi = NewsApiClient(api_key=API_KEY)

    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(q=stock,
                                              sources='bbc-news,the-verge',
                                              language='en')
    save_data.save_json(top_headlines, "top_headlines")

    # /v2/everything
    # TODO: Get current date and retrieve news from previous 2 days
    everything = newsapi.get_everything(q=company,
                                        from_param='2021-01-01',
                                        to='2021-01-07',
                                        language='en',
                                        sort_by='relevancy',
                                        page_size=3,
                                        page=1)
    save_data.save_json(everything, "everything")

    # /v2/sources
    sources = newsapi.get_sources(language="en")
    save_data.save_json(sources, "sources")


def newsapi_requests(stock, company):
    """
    Using Python requests module -
    Note that http requests uses camelCase in parameter names:
    excludeDomains, from_param, sortBy, pageSize, apiKey
    """

    base_url = "https://newsapi.org/"

    endpoint_top_headlines = "v2/top-headlines"
    parameters_top_headlines = {"q": stock,
                                "sources": 'bbc-news,the-verge',
                                "language": 'en',
                                "apiKey": API_KEY,
                                }

    # TODO: Get current date and retrieve news from previous 2 days
    endpoint_everything = "v2/everything"
    parameters_everything = {"q": company,
                             "from": '2021-01-01',
                             "to": '2021-01-07',
                             "language": 'en',
                             "sortBy": 'relevancy',
                             "pageSize": 3,
                             "page": 1,
                             "apiKey": API_KEY,
                             }

    endpoint_sources = "v2/sources"
    parameters_sources = {"language": 'en',
                          "apiKey": API_KEY,
                          }

    url = base_url + endpoint_everything

    response = requests.get(url=url, params=parameters_everything, timeout=1)
    response.raise_for_status()

    everything = response.json()
    save_data.save_json(everything, "everything")

