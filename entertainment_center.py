# This file create a list  movies objects
# Movies attribute is obtained using
# https://www.themoviedb.org/documentation/api
# then create HTML file to display movie list
# Done by : Nadia Ahmed

import media
import fresh_tomatoes
import urllib2
import json


def Format_Query(movie_name):
    """ This method take a string
        movie_name and return it in
        query format
    """
    # split string into a list
    movie_split = movie_name.split()
    movie_query = ""
    count = len(movie_split)
    # loop to add + in the query
    for temp in movie_split:
        count = count-1
        if count != 0:
            movie_query += temp+"+"
        else:
            movie_query += temp
    return movie_query


def Create_Movie(movie_name):
    """ This method take movie name,
        search for it's id in API,
        using id it will get from API
        title, poster path and trailer.
        Return movie object
        """

    # get the movie query format
    movie_query = Format_Query(movie_name)
    # API key obtained from movie data base
    api_key = "0f94ac859ae6c98a13091faf91e75cf2"
    # search for movie by name to ge the id from
    # https://www.themoviedb.org/documentation/api
    url_search_name = "https://api.themoviedb.org/3/search/movie?api_key="+api_key+"&query="+movie_query
    response2 = urllib2.urlopen(url_search_name)
    data2 = json.loads(response2.read())
    # extract movie id if the query search has a result
    if data2['total_results'] != 0:
        # extract movie id
        movie_id = data2['results'][0]['id']
        # search movie by id ,url include videos respons
        url3 = "http://api.themoviedb.org/3/movie/"+str(movie_id)+"?api_key="+api_key+"&append_to_response=videos"
        response = urllib2.urlopen(url3)
        data = json.loads(response.read())
        # exract movie title from json
        movie_title = data['title']
        # extract movie poster path
        poster_path = data['poster_path']
        # extract the youtube video trailer key
        video_key = data['videos']['results'][0]['key']
        # poster path http://image.tmdb.org/t/p/ formate
        url_image = "http://image.tmdb.org/t/p/"+"/w342"+data['poster_path']
        # the trailer path
        url_video = "https://www.youtube.com/watch?v="+video_key
        Movie1 = media.Movie(movie_title, url_image, url_video)
        return Movie1
    # return None if the movie name dose not found in API
    else:
        return None


def Create_List(Movie_name_list):
    """ This method take array
        of string movie name
        and return list of movie objects
    """
    # creating the list movies
    movies_list = []
    for name in Movie_name_list:
        M1 = Create_Movie(name)
        # if valid movie returned added to list
        if M1 != None:
            movies_list.append(M1)
        # esle update user if movie not found in API
        else:
            print "Movie titled: "+name+" not found in the data base "
    return movies_list

# Create Movie List
movies_name = ["The Ring", "The Hitman's Bodyguard ", "Taken", "Hangover",
               "Die Hard", "The others", "Ocean's Eleven",
               "The Dark Knight", "Jumanji: Welcome to the Jungle "]
print "Wait till movies been loaded"

movies_list = Create_List(movies_name)
# creates an HTML file
fresh_tomatoes.open_movies_page(movies_list)
