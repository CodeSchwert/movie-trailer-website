"""The MIT License (MIT)

Copyright (c) <year> <copyright holders>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import webbrowser


class Movie(object):
    """Movie information class.

    Movie class holds information about the movie title, genre, MPAA rating
    (taken from the IMDB website), plus links to the movie trailer on YouTube,
    movie poster image on Wikipedia, and movie IMDB website.

    Attributes:
        title: The movie title.
        tagline: The movie tagline, most likely taken from IMDB.
        poster_image_url: URL to a image of the movie poster.
        trailer_youtube_url: URL to the movie trailer on YouTube.
        imdb_url: Link to the movie IMDB website.
        mpaa_rating: MPAA rating, as taken from IMDB.
        genre: Genre type of the movie. Should be a string formatted as follow:
            "Drama | Thriller | Comedy".
    """

    def __init__(self, movie_title, mpaa_rating, genre, movie_tagline,
                 poster_image, imdb_url, youtube_url):
        """Initializes the class with relevant movie information."""
        self.title = movie_title
        self.mpaa_rating = mpaa_rating
        self.genre = genre
        self.tagline = movie_tagline
        self.poster_image_url = poster_image
        self.imdb_url = imdb_url
        self.trailer_youtube_url = youtube_url
