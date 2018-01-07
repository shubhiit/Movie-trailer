# import inbuild module webbrowser and use it's methods as required
import webbrowser


class Movie():
    """
    creating a class "Movie"
    class to create instance of a movie with the required details of it
        Consists of:
        variables which stores required details of the movie
        method to connect with the URL of trailer
    """

    # declare init function which will run as soon as a instance is created
    def __init__(
        self,
        movie_title,
        movie_storyline,
        trailer_youtube,
        poster_image,
                ):
        # allocate values to instance variables with self keyword
        # name of the movie
        self.title = movie_title
        # storyline of the movie
        self.storyline = movie_storyline
        # URL for poster of movie
        self.poster_image_url = poster_image
        # URL for trailer of movie
        self.trailer_youtube_url = trailer_youtube

    # function created to launch the trailer using url of the trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
