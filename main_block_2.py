""" The function in this file returns the movie that the user should watch based on the already existing movies
in the graph, by comparing each movie score to the user score. """
import random
import moviegraph


def watch_next(network: moviegraph.MovieNetwork, user_score: int) -> str:
    """Returns an ideal movie to watch next based on the smallest difference between the movie score and the user
    score."""

    dict_so_far = {}
    for movie in network.movies:
        dict_so_far[movie] = abs(network.movies[movie].score - user_score)
    min_diff = min([dict_so_far[movie] for movie in dict_so_far])

    list_of_possible_movies = []
    for movie1 in dict_so_far:
        if dict_so_far[movie1] == min_diff:
            list_of_possible_movies.append(movie1)
    if len(list_of_possible_movies) == 1:
        movie_to_watch = list_of_possible_movies.pop()
        network.add_movie_or_user('user', user_score, 'users')
        network.add_neighbour(movie_to_watch, 'user', 'users')
        return movie_to_watch
    else:
        movie_to_watch = random.choice(list_of_possible_movies)
        network.add_movie_or_user('user', user_score, 'users')
        network.add_neighbour(movie_to_watch, 'user', 'users')
        return movie_to_watch
