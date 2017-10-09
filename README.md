# Movie_Trailer_Website
Source code for a Movie Trailer website.
By Omar Gaber Abdelmaksoud.

This is the **first** project made for fulfillment of [Udacity's Full Stack Web Development Nanodegree Program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

##Abstract
The project's main focus was to consolidate the concept of OOP using Python. The hands-on implementation was to create a server side code to store a list of my favorite movies along with the movies' poster images and also the YouTube trailer URLs.

##Requirements
* To run this project, you need to have **Python 2.7** installed on your machine. Download the release best suited for your machine through this [link](https://www.python.org/download/releases/2.7/)

##Running the Project
* You first need to fork this repo to create your own copy on GitHub. For instructions on how to fork a repo on GitHub, click [here](https://help.github.com/articles/fork-a-repo/)
* Next to that, clone the repo you just forked to get a local version of the source code in the repo. For instructions on how to clone a repo, click [here](https://help.github.com/articles/cloning-a-repository/)
* Access the cloned repo and run the file **website.py**. You can run it either via terminal command `python website.py` or through the GUI from your IDE.
* A webpage will open on your default browser and a list of my favorite movies will appear along with their poster images and storylines will appear. On clicking on any of the movies, a pop-up box playing the movie's trialer will show up.


##Adding your own favorite movies.
To add your favorite movie, you need to access the **website.py** file to enter some modifications for your movie to be added to the webpage.

###Adding your favorite movie.
* Open **website.py** in your editor.
* Let's say for instance you want to add the movie, and let it be Inception for example. To add the movie, enter the following snippet:
`inception = media.Movie("Inception", "Dom Cobb is a thief with the rare ability to enter people's dreams and steal their secrets from their subconscious.", "http://t2.gstatic.com/images?q=tbn:ANd9GcRo9vfJCM6dzPkZHIHBVCtlJnAnew9Ai26kEdrli0-tfmatmciD", "https://www.youtube.com/watch?v=YoHD9XEInc0")` 
* The previous line creates an instance of the Movie class called inception and passes it its name, storyline, poster image url and YouTube trailer url. It's exactly in the order stated.
* Next to that, in the list called movies declared after the movies' instances created, add **inception** to the list of movies.
* The function `open_movies_page` is declared in `fresh_tomatoes.py` and it takes the movies list and generates the static webpage we need to display the list of your favorite movies.
# Movie_Trailer
