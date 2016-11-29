#The import statement allow us to define classes in different files than the instances of classes.  By importing, we can use the functions that are defined in different files.

import media
import fresh_tomatoes

#These statements assign to a variable new instances of the class Movie and populates it with information.

top_gun = media.Movie("Top Gun", "55", "https://images-na.ssl-images-amazon.com/images/M/MV5BZjQxYTA3ODItNzgxMy00N2Y2LWJlZGMtMTRlM2JkZjI1ZDhhXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://youtu.be/ioWpe3hdFH0")

argo = media.Movie("Argo", "96", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc3MjI0MjM0NF5BMl5BanBnXkFtZTcwMTYxMTQ1OA@@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://youtu.be/w918Eh3fij0")

forrest_gump = media.Movie("Forrest Gump", "72", "https://images-na.ssl-images-amazon.com/images/M/MV5BYThjM2MwZGMtMzg3Ny00NGRkLWE4M2EtYTBiNWMzOTY0YTI4XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_UY268_CR10,0,182,268_AL_.jpg", "https://youtu.be/uPIEn0M8su0")

lincoln = media.Movie("Lincoln", "90", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQzNzczMDUyNV5BMl5BanBnXkFtZTcwNjM2ODEzOA@@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://youtu.be/KJVuqYkI2jQ")

license_to_drive = media.Movie("License to Drive", "18", "https://images-na.ssl-images-amazon.com/images/M/MV5BOTk1OWUyODgtMDBlMC00ZDdlLWIzOWUtYTBjNzQ1M2ZjOThiXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://youtu.be/a4KJtDxTqWQ")

animal_house = media.Movie("Animal House", "91", "https://images-na.ssl-images-amazon.com/images/M/MV5BM2M2ZDA4MTYtOGRjMi00OTg5LWI1ZTUtMjQxZTc2NWZjNDFkXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://youtu.be/KWjtI6n5xWM")

christmas_vacation = media.Movie("Christmas Vacation", "64", "https://images-na.ssl-images-amazon.com/images/M/MV5BMGZkMWQ2MzMtYTkxYS00OThmLWI0ZTQtNmY0ZTkyY2E4MjliXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://youtu.be/NBTTipJX-h4")

fear_and_loathing = media.Movie("Fear and Loathing in Las Vegas", "49", "https://images-na.ssl-images-amazon.com/images/M/MV5BNjA2ZDY3ZjYtZmNiMC00MDU5LTgxMWEtNzk1YmI3NzdkMTU0XkEyXkFqcGdeQXVyNjQyMjcwNDM@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://youtu.be/8m662obIvhY")

star_trek_II = media.Movie("Star Trek II", "88", "https://images-na.ssl-images-amazon.com/images/M/MV5BMzcyYWE5YmQtNDE1Yi00ZjlmLWFlZTAtMzRjODBiYjM3OTA3XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://youtu.be/vBpwPfW1Lsw")

#This is an array of the movie variables that we have created above.

movies = [top_gun, argo, forrest_gump, lincoln, license_to_drive, animal_house, christmas_vacation, fear_and_loathing, star_trek_II]

#Here we are calling the open_movies_page function defined in the fresh_tomatoes.py file and passing the movies array as the argument.  The fresh_tomatoes file lays out the HTML structure of the webpage and then populates it with the movie information contained in the variables.

fresh_tomatoes.open_movies_page(movies)