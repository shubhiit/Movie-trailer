# import movie.py to use Movie class for it's variable and methods
import movie
# import presentation.py to use Methods and improve presentation of page
import presentation

# creating objects of Movie class with providing value of the variables
toy_story = movie.Movie("Toy Story",
                        "A story of a boy and its toy which come to life",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-wt2it4_fbf729c8.jpeg?region=0,0,300,450"  # noqa
                        )
conjuring_2 = movie.Movie("The Conjuring-2",
                          "A teenager possessed in a haunted house",
                          "https://www.youtube.com/watch?v=VFsmuRPClr4",
                          "http://t3.gstatic.com/images?q=tbn:ANd9GcTW7MdBhKKtzWRoy4gtHR7YZ2hv6ln1cxpZCNwnXAR8dHPDz-eO"  # noqa
                          )
insidious = movie.Movie("Insidious: The Last Key",
                        "Movie yet to come",
                        "https://www.youtube.com/watch?v=VT80sdgXSAM",
                        "http://www.moviehouse.co.uk/Media/2b494090-6c21-475a-9cf8-f9cc3134555e.jpg"  # noqa
                        )
# to launch the web page
presentation.open_movies_page([toy_story, conjuring_2, insidious])
