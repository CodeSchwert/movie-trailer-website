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

import fresh_tomatoes
import movie

# movie.Movie(movie_title, mpaa_rating, genre, movie_tagline, poster_image, imdb_url, youtube_url)

howls_moving_castle = movie.Movie("Howl's Moving Castle", "PG",
                                  "Animation | Adventure | Family | Fantasy",
                                  "Hauru no ugoku shiro",
                                  "http://upload.wikimedia.org/wikipedia/en/a/a0/Howls-moving-castleposter.jpg",
                                  "http://www.imdb.com/title/tt0347149/?ref_=nv_sr_1",
                                  "https://www.youtube.com/watch?v=iwROgK94zcM")

knights_of_badassdom = movie.Movie("Knights of Badassdom", "R",
                                   "Adventure | Comedy | Fantasy | Horror",
                                   "'Tis about to get medieval up in here.",
                                   "http://upload.wikimedia.org/wikipedia/en/4/43/Knights_of_Badassdom.jpg",
                                   "http://www.imdb.com/title/tt1545660/?ref_=nv_sr_2",
                                   "https://www.youtube.com/watch?v=zyougFDZ7zU")

life_of_brian = movie.Movie("Life of Brian", "R",
                            "Comedy",
                            "Just when you thought you were saved...",
                            "http://upload.wikimedia.org/wikipedia/en/1/18/Lifeofbrianfilmposter.jpg",
                            "http://www.imdb.com/title/tt0079470/?ref_=nv_sr_4",
                            "https://www.youtube.com/watch?v=TKPmGjVFbrY")

the_matrix = movie.Movie("The Matrix", "R", "Action | Sci-Fi",
                         "Reality is a thing of the past.",
                         "http://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "http://www.imdb.com/title/tt0133093/?ref_=nv_sr_1",
                         "https://www.youtube.com/watch?v=vKQi3bBA1y8")

the_dark_knight = movie.Movie("The Dark Kinght", "PG-13",
                              "Action | Crime | Drama",
                              "Out of the darkness...comes the Knight.",
                              "http://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Dark_Knight.jpg/220px-Dark_Knight.jpg",
                              "http://www.imdb.com/title/tt0468569/?ref_=fn_al_tt_1",
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY")

edge_of_tomorrow = movie.Movie("Edge iof Tomorrow", "PG-13",
                               "Action | Adventure | Mystery | Sci-Fi",
                               "Live. Die. Repeat.",
                               "http://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg",
                               "http://www.imdb.com/title/tt1631867/?ref_=nv_sr_1",
                               "https://www.youtube.com/watch?v=yUmSVcttXnI")

movies = [howls_moving_castle, knights_of_badassdom, life_of_brian, the_matrix,
          the_dark_knight, edge_of_tomorrow]

fresh_tomatoes.open_movies_page(movies)
