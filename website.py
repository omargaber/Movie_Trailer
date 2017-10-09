import media
import fresh_tomatoes

#Instances Created of the class Movie, defined in media
#Each instance (object) is given the movie title, storyline, poster image URL and the YouTube trailer URL.

dead_poet_society = media.Movie("Dead Poets Society",
	"A new English teacher, John Keating, is introduced to an all-boys preparatory school that is known for its ancient traditions and high standards. He uses unorthodox methods to reach out to his students, who face enormous pressures from their parents and the school.",
	"http://t1.gstatic.com/images?q=tbn:ANd9GcSFiizcraYyxtIB2imVhFaWB5eMW1m95_Hp42MVj8Ngxo3Eq386",
	"https://www.youtube.com/watch?v=4lj185DaZ_o")

scent_of_a_woman = media.Movie("Scent of a Woman",
	"Frank is a retired Lt. Col. in the US army. He's blind and impossible to get along with. Charlie is at school and is looking forward to going to college. To help pay for a trip home for Christmas, he agrees to look after Frank over Thanksgiving.",
	"http://t0.gstatic.com/images?q=tbn:ANd9GcTwsF1qzE70DGGnbWGVHTDJvQk-dBofclze25rTvhgT9lV0-psJ",
	"https://www.youtube.com/watch?v=8ql_xsAByKk")

good_will_hunting = media.Movie("Good Will Hunting",
	"Will Hunting has a genius-level IQ but chooses to work as a janitor at MIT. When he solves a difficult graduate-level math problem, his talents are discovered by Professor Gerald Lambeau, who decides to help the misguided youth reach his potential.",
	"http://t0.gstatic.com/images?q=tbn:ANd9GcT4vHOLWBM56R6fNs7K9xcEf7V8M8mzrzi6LtWGXrqfg8-KynGn",
	"https://www.youtube.com/watch?v=7TSLzPu2no4")

hacksaw_ridge = media.Movie("Hacksaw Ridge",
	"The true story of Pfc. Desmond T. Doss, who won the Congressional Medal of Honor despite refusing to bear arms during WWII on religious grounds. Doss was drafted and ostracized by fellow soldiers for his pacifist stance but went on to earn respect and adoration for his bravery, selflessness and compassion after he risked his life -- without firing a shot -- to save 75 men in the Battle of Okinawa.",
	"http://t1.gstatic.com/images?q=tbn:ANd9GcQkB0TuKruaG_PylU3qlUC2BkFKj3R4aUgN2MMDkc7hmSXrPTsy",
	"https://www.youtube.com/watch?v=s2-1hz1juBI")

saving_private_ryan = media.Movie("Saving Private Ryan",
	"Captain John Miller takes his men behind enemy lines to find Private James Ryan, whose three brothers have been killed in combat. Surrounded by the brutal realties of war, while searching for Ryan, each man embarks upon a personal journey and discovers their own strength to triumph over an uncertain future with honor, decency and courage.",
	"http://is5.mzstatic.com/image/thumb/Video/v4/66/83/44/668344c7-a8fa-107c-72f9-b1fdceb226c6/source/1200x630bb.jpg",
	"https://www.youtube.com/watch?v=zwhP5b4tD6g")

cast_away = media.Movie("Cast Away",
	"Obsessively punctual FedEx executive Chuck Noland is en route to an assignment in Malaysia when his plane crashes over the Pacific Ocean during a storm. The sole survivor of the flight, Chuck washes ashore on a deserted island. When his efforts to sail away and contact help fail, Chuck learns how to survive on the island, where he remains for years, accompanied by only his handmade volleyball friend, Wilson. Will Chuck ever return to civilization and reunite with his loved ones?",
	"https://static.rogerebert.com/uploads/movie/movie_poster/cast-away-2000/large_w515BrZvczKIxbHurG6HIiYYrba.jpg",
	"https://www.youtube.com/watch?v=PJvosb4UCLs")

forrest_gump = media.Movie("Forrest Gump",
	"Slow-witted Forrest Gump has never thought of himself as disadvantaged, and thanks to his supportive mother, he leads anything but a restricted life. Whether dominating on the gridiron as a college football star, fighting in Vietnam or captaining a shrimp boat, Forrest inspires people with his childlike optimism. But one person Forrest cares about most may be the most difficult to save -- his childhood love, the sweet but troubled Jenny.",
	"https://vignette4.wikia.nocookie.net/f__/images/e/ef/Forrest-gump-poster-1994-tom-hanks.png/revision/latest?cb=20130922155301&path-prefix=forrestgump",
	"https://www.youtube.com/watch?v=uPIEn0M8su0")

pursuit_of_happyness = media.Movie("Pursuit of Happyness",
	"Life is a struggle for single father Chris Gardner. Evicted from their apartment, he and his young son find themselves alone with no place to go. Even though Chris eventually lands a job as an intern at a prestigious brokerage firm, the position pays no money. The pair must live in shelters and endure many hardships, but Chris refuses to give in to despair as he struggles to create a better life for himself and his son.",
	"https://fontmeme.com/images/The-Pursuit-of-Happyness-Poster.jpg",
	"https://www.youtube.com/watch?v=SYg7RRYKWGw")

the_circle = media.Movie("The Circle",
	"Mae Holland seizes the opportunity of a lifetime when she lands a job with the world's most powerful technology and social media company. Encouraged by the company's founder, Mae joins a groundbreaking experiment that pushes the boundaries of privacy, ethics and personal freedom. Her participation in the experiment, and every decision she makes soon starts to affect the lives and futures of her friends, family and that of humanity.",
	"http://celebmafia.com/wp-content/uploads/2017/04/emma-watson-the-circle-movie-photos-and-posters-12.jpg",
	"https://www.youtube.com/watch?v=QCOXARv6J9k")



#A list called movies stores all of the instances (objects) created
movies = [dead_poet_society, scent_of_a_woman, good_will_hunting, hacksaw_ridge, saving_private_ryan, cast_away, forrest_gump, pursuit_of_happyness, the_circle]


#Generating a static webbpage by calling the function "open_movies_page" declared in fresh_tomatoes.py
#The function is given the list of movies as a parameter in order to display it on the browser
fresh_tomatoes.open_movies_page(movies)
