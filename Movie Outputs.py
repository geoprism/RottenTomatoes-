#Brian Wong
#This module handle all outputs

# 1.) Search movie: returns movie title, critic score, audience score
# 2.) Show top dvd rental by popularity, then show top dvd rental by
#     critic/audience score mean
# 3.) Show top dvd new release by critic/audience score mean

import random
BASE_RT_URL = 'http://api.rottentomatoes.com/api/public/v1.0/'
RT_API_KEY = 'ew937yyznfu3gvdt5rh2g4cc'

#info type
movie_search_url = 'movies.json?'
new_release_dvd = 'lists/dvds/new_releases.json?'
top_rentals = 'lists/dvds/top_rentals.json?'
movie_review = 'movies/[MOOOOOOVIEEEE IDDDD]/reviews.json?' #NOT WORKABLE YET


import movie_api



def movie_search() -> None:
    """
    1.) Search movie: returns movie title, critic score, audience score
    """
    while True:
        movie = input('Movie: ')
        url = movie_api.build_url(movie,3,movie_search_url)
        json_result = movie_api.json_response(url)
        print()
        if json_result['total'] != 0:
            for movie in json_result['movies']:
            
                print('{} ({})'.format(movie['title'],movie['year']))
                print('Critics Rating: {}'.format(_ratings(movie['ratings']['critics_score'])))
                print('Audience Rating: {}%'.format(movie['ratings']['audience_score']))
                print()
            break
        
        print('Sorry, no results for "{}", try again'.format(movie))
        print()

def _ratings(rating:int):
    """checks if there are any rating for a movie"""
    if rating == -1:
        return('No critic reviews')
    return(str(rating)+'%')


def top_ten_rental() -> None:
    """Shows top ten movies by popularity"""
    url = movie_api.top_rental_build_url('',10,top_rentals)
    json_result = movie_api.json_response(url)
    print()
    print('Top Rentals by Popularity')
    print('-------------------------')
    print()
    for movie in json_result['movies']:
        print('{} ({})'.format(movie['title'],movie['year']))
        print('Critics Rating: {}'.format(_ratings(movie['ratings']['critics_score'])))
        print('Audience Rating: {}%'.format(movie['ratings']['audience_score']))
        print()

def best_movies_from_top_rental()-> None:
    """
    Allows user to enter baseline score, returns movie from top rentals
    """
    url = movie_api.top_rental_build_url('',50,top_rentals)
    json_result = movie_api.json_response(url)
    baseline = input('Baseline score for a good movie: ')
    print()
    print('MOVIES WORTH WATCHING:')
    for movie in json_result['movies']:
        if (((movie['ratings']['critics_score'])+(movie['ratings']['critics_score']))/2)>int(baseline):
            print(movie['title'])

def golden_movies()->None:
    """
    prints golden movies from top rentals
    """
    url = movie_api.top_rental_build_url('',50,top_rentals)
    json_result = movie_api.json_response(url)
    print("GOLDEN AKA PREMIUM MOVIES")
    print("-------------------------")
    print()
    baseline_reviews = input('Miniumum number of reviews: ')
    baseline_score = input('Baseline score for a golden movie: ')
    movies = []
    try:
        for movie in json_result['movies']:
            movie_id = movie['id']
            review_url = movie_api.golden_rental_url(movie_id)
            json_review = movie_api.json_response(review_url)
            if json_review['total']>int(baseline_reviews) and (((movie['ratings']['critics_score'])+
                                              (movie['ratings']['critics_score']))/2)>int(baseline_score):
                
                #movies.append(movie['title'])
                print(movie['title'])
    except:
        print('error')
    #return movies

def rand_golden_movie()->str:
    movies = golden_movies()
    print(movies)
    movie = random.choice(movies)
    print('You should watch: {}'.format(movie))

    
if __name__ == '__main__':
    movie_search()
    #top_ten_rental()
    #best_movies_from_top_rental()
    #golden_movies()
    #rand_golden_movie()
