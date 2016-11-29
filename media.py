#Importing the webbrowser allows us to open a web browser by running the .py file in the terminal.
import webbrowser

#This is the constructor function for every instance of the Movie class.  The init function takes in the movie information that the user has specified, assigns it to a variable, and creates a new instance for that particular movie.   

class Movie():
	# This class provides a way to store movie related information
	def __init__(self, movie_title, RT_score, poster_image, trailer_youtube):
		# initialize instance of class Movie
		self.title = movie_title
		self.RT_score = RT_score #Rotten Tomatoes score
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
