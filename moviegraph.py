
"""
This file contains the code for the construction of the Movie graph network, including the User and
Movie Classes which will mainly be interacting with the network.

"""


class Movie:
    """
    A class representation for a Movie to be connected in a network, then connected with a User.
    Instance Attributes:
    - name: a string containing the name of the movie
    - score: an integer representing the computed score of the movie
    - neighbours: a dictionary mapping neighbours to the Movie. The name of the neighbour Movie is
      mapped to the neighbour Movie's score

    """
    name: str
    score: int
    neighbours: dict[str: int]

    def __init__(self, name: str, score: int) -> None:
        """Initialize this Movie with the given name and score and no connections to any neighbour Movies."""
        self.name = name
        self.score = score
        self.neighbours = {}


class User:
    """
    A class representation for the user, who is answering the questionnare.
    Instance Attributes:
    - score: the score associated with the user, which is accumulated
    through the user's answering of the questionnare
    - movie: a dictionary mapping the score of the movie closest to the score of the user, to the Movie

    """
    score: int
    movie: dict[int, Movie]

    def __init__(self, score: int) -> None:
        """Initialize this user with the given score and no connections to any movies."""
        self.score = score
        self.movie = {}


class MovieNetwork:
    """
    A class representation for the network connection of Movies, which
    will be used to connect the perfect Movie with a user.
    Instance Attributes:
    - movies: A mapping from Movie name to Movie in this network


    """
    movies: dict[str: Movie]

    def __init__(self) -> None:
        """Initialize this empty network """
        self.movies = {}

    def add_movie(self, title: str, score: int) -> Movie:
        """Add a movie with the given name to the network """
        movie = Movie(title, score)
        self.movies[title] = Movie(title, score)
        return movie

    def add_neighbour(self, title1: str, title2: str) -> None:
        """Add a neighbour between the two movies with the given titles in this network.

        Raise a ValueError if title1 or title2 are not in the network.

        Preconditions:
            - title1 != title2
        """
        if title1 in self.movies and title2 in self.movies:
            v1 = self.movies[title1]
            v2 = self.movies[title2]
            v1.neighbours[title2] = v2.score
            v2.neighbours[title1] = v1.score
        else:
            raise ValueError


def movienetworkcreate(net: MovieNetwork, characteristics: dict) -> MovieNetwork:
    """Create a complete Movienetwork to be used in the sorting algorithm, using the
     dictionary of movie names to scores"""
    center_node = net.add_movie('all movies', 0)
    num_movies = len(characteristics)
    movie_names = list(characteristics.keys())
    for chara in characteristics:
        net.add_movie(chara, characteristics[chara])
    for movie in range(0, num_movies - 1):
        net.add_neighbour(movie_names[movie + 1], movie_names[movie])
    for movie in range(0, num_movies):
        net.add_neighbour(center_node.name, movie_names[movie])
    return net
