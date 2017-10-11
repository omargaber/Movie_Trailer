import media
import fresh_tomatoes

# Instances Created of the class Movie, defined in media
# Each instance has a title, storyline, poster image URL & YouTube trailer URL


dead_poet_society = media.Movie("Dead Poets Society",
                                """A new English teacher is introduced to all-boys prep school known for its ancient traditions & high standards.""",
                                """http://t1.gstatic.com/images?q=tbn:ANd9GcSFiizcraYyxtIB2imVhFaWB5eMW1m95_Hp42MVj8Ngxo3Eq386""",
                                """https://www.youtube.com/watch?v=4lj185DaZ_o""")

scent_of_a_woman = media.Movie("Scent of a Woman",
                               """Frank is a retired Lt. Col. He's blind and impossible deal with. Charlie looks after Frank to help pay for a trip back home.""",
                               """http://t0.gstatic.com/images?q=tbn:ANd9GcTwsF1qzE70DGGnbWGVHTDJvQk-dBofclze25rTvhgT9lV0-psJ""",
                               """https://www.youtube.com/watch?v=8ql_xsAByKk""")

good_will_hunting = media.Movie("Good Will Hunting",
				"""A janitor with a high IQ works at MIT. His capabilities of solving difficult math problems encuourages a professor to guide him to achieve his full potential""",
				"""http://t0.gstatic.com/images?q=tbn:ANd9GcT4vHOLWBM56R6fNs7K9xcEf7V8M8mzrzi6LtWGXrqfg8-KynGn""",
				"""https://www.youtube.com/watch?v=7TSLzPu2no4""")

hacksaw_ridge = media.Movie("Hacksaw Ridge",
			    """The true story of Pfc. Doss, who won the Congressional Medal of Honor despite refusing to bear arms during WWII on religious grounds.""",
			    """http://t1.gstatic.com/images?q=tbn:ANd9GcQkB0TuKruaG_PylU3qlUC2BkFKj3R4aUgN2MMDkc7hmSXrPTsy""",
			    """https://www.youtube.com/watch?v=s2-1hz1juBI""")

saving_private_ryan = media.Movie("Saving Private Ryan",
				  """Captain Miller takes his men behind enemy lines to find Private Ryan, whose three brothers have been killed in combat.""",
				  """http://is5.mzstatic.com/image/thumb/Video/v4/66/83/44/668344c7-a8fa-107c-72f9-b1fdceb226c6/source/1200x630bb.jpg""",
				  """https://www.youtube.com/watch?v=zwhP5b4tD6g""")

cast_away = media.Movie("Cast Away",
			"""Obsessively punctual FedEx executive is en route to an assignment in Malaysia when his plane crashes over the Pacific Ocean during a storm.""",
			"""https://static.rogerebert.com/uploads/movie/movie_poster/cast-away-2000/large_w515BrZvczKIxbHurG6HIiYYrba.jpg""",
			"""https://www.youtube.com/watch?v=PJvosb4UCLs""")

forrest_gump = media.Movie("Forrest Gump",
			   """Slow-witted Forrest Gump has never thought of himself as disadvantaged, and thanks to his supportive mother, he leads anything but a restricted life.""",
			   """https://vignette4.wikia.nocookie.net/f__/images/e/ef/Forrest-gump-poster-1994-tom-hanks.png/revision/latest?cb=20130922155301&path-prefix=forrestgump""",
			   """https://www.youtube.com/watch?v=uPIEn0M8su0""")

pursuit_of_happyness = media.Movie("Pursuit of Happyness",
				   """Life is a struggle for single father who gets evicted from their apartment, he and his young son find themselves alone with no place to go.""",
				   """https://fontmeme.com/images/The-Pursuit-of-Happyness-Poster.jpg""",
				   """https://www.youtube.com/watch?v=SYg7RRYKWGw""")

the_circle = media.Movie("The Circle",
			 """Mae Holland seizes the opportunity of a lifetime when she lands a job with the world's most powerful technology and social media company.""",
			 """http://celebmafia.com/wp-content/uploads/2017/04/emma-watson-the-circle-movie-photos-and-posters-12.jpg""",
			 """https://www.youtube.com/watch?v=QCOXARv6J9k""")

# A list called movies stores all of the instances (objects) created
movies = [
    dead_poet_society,
    scent_of_a_woman,
    good_will_hunting,
    hacksaw_ridge,
    saving_private_ryan,
    cast_away,
    forrest_gump,
    pursuit_of_happyness,
    the_circle
]


# Generating a static webbpage by calling the function "open_movies_page"
# The function is given a list of movies to display it in the browser
fresh_tomatoes.open_movies_page(movies)
