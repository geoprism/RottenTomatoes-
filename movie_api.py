#Brian Wong
# 1.) build RT url, make http request, parse the JSON response
# 2.) return movie title, year, ratings, critics_score, audience_score

import urllib.parse
import urllib.request
import json


BASE_RT_URL = 'http://api.rottentomatoes.com/api/public/v1.0/'
RT_API_KEY = 'ew937yyznfu3gvdt5rh2g4cc'
#info type
movie_search = 'movies.json?'
new_release_dvd = 'lists/dvds/new_releases.json?'
top_rentals = 'lists/dvds/top_rentals.json?'
movie_review = 'movies/[MOOOOOOVIEEEE IDDDD]/reviews.json?' #NOT WORKABLE YET


def build_url(movie: str, max_results:int, info_type: str)->str:
    """returns encoded url"""
    query_parameters = [('apikey', RT_API_KEY),('q', movie),('page_limit', max_results)]

    #print(query_parameters)

    return BASE_RT_URL + info_type + urllib.parse.urlencode(query_parameters)

def top_rental_build_url(movie: str, max_results:int, info_type: str)->str:
    """returns encoded url"""
    query_parameters = [('apikey', RT_API_KEY),('q', movie),('limit', max_results)]

    return BASE_RT_URL + info_type + urllib.parse.urlencode(query_parameters)

def golden_rental_url(movie_id: str)-> str:
    query_parameters = [('apikey',RT_API_KEY),('review_type', 'all')]
    return (BASE_RT_URL+'movies/'+movie_id+'/reviews.json?' +urllib.parse.urlencode(query_parameters))

def json_response(url:str)-> 'json':
    """Takes URL and returns Python object representing JSON response"""

    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    finally:
        if response != None:
            response.close()
            




