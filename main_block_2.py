import csv

# This takes the list of movies and outputs the desired charactersitics as a list of lists
def reader1(file: str) -> list[list]:
    """Take the csv file and return a list of all the movies and their characteristics."""
    with open(file) as csv_file:
        reader = csv.reader(csv_file)
        lst_of_movies = []
        for row in reader:
            movie_lst = []
            movie_lst.append(row[1])
            movie_lst.append(row[0])
            movie_lst.append(row[5][1:])
            movie_lst.append(int(row[4]))
            movie_lst.append(float(row[3]))
            movie_lst.append(row[0])
            movie_lst.append(row[2])
            lst_of_movies.append(movie_lst)
        return lst_of_movies
