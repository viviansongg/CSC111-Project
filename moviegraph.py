from python_ta.contracts import check_contracts

class Movie:
    """

    """
    name: str
    score: int
    neighbours: dict[str: int]

    def __init__(self, name: str, score: int) -> None:
        """Initialize this user with the given address and no connections to any movies."""
        self.name = name
        self.score = score
        self.neighbours = {}


class User:
    """
    A class representation for the user, who is answering the questionnare.
    Instance Attributes:
    - score: the score associated with the user, which is accumulated through the user's answering of the questionnare

    """
    score: int
    movie: dict[int, Movie]

    def __init__(self, score: int) -> None:
        """Initialize this user with the given score and no connections to any movies."""
        self.score = score
        self.movie = {}


class MovieNetwork:
    """

        """
    movies: dict[str: Movie]

    def __init__(self) -> None:
        """Initialize this user with the given address and no connections to any movies."""
        self.movies = {}

    def add_movie(self, item: str, score: int) -> Movie:
        """Initialize this user with the given address and no connections to any movies."""
        movie = Movie(item, score)
        self.movies[item] = Movie(item, score)
        return movie

    def add_neighbour(self, item1: str, item2: stry) -> None:
        """Add an edge between the two vertices with the given items in this graph.

        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.

        Preconditions:
            - item1 != item2
        """
        if item1 in self.movies and item2 in self.movies:
            v1 = self.movies[item1]
            v2 = self.movies[item2]
            v1.neighbours[item2] = v2
            v2.neighbours[item1] = v1
        else:
            raise ValueError

def movienetworkcreate(net: MovieNetwork, characteristics: dict) -> MovieNetwork:
    """Initialize this user with the given address and no connections to any movies."""
    center_node = net.add_movie('all movies', 0)
    for c in characteristics:
        net.add_movie(c, characteristics[c])
        net.add_neighbour(center_node.name, c)
    return net
