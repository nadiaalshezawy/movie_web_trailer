# This file define movie class , each object has
#movie titles, poster images, and movie trailer URLs


class Movie():
    """ This class provide a way to store movie related information"""

    def __init__(self, movie_title,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
