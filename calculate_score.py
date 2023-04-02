"""Computing Scores for Movies for a dataset.
"""
import csv


def calculate_score1(movie_file: str) -> dict:
    """Returns a dictionary mapping each movie in the csv file to its associated score.
    """
    movie_scores = {}
    with open(movie_file) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            # question 1
            genre = row[5]
            genre = genre.strip("[']")
            if genre == 'Romance':
                answer1 = 100000
            elif genre == 'Comedy':
                answer1 = 200000
            elif genre == 'Action':
                answer1 = 300000
            elif genre == 'Horror':
                answer1 = 400000
            elif genre == 'Thriller':
                answer1 = 500000
            elif genre == 'Adventure':
                answer1 = 600000
            elif genre == 'Crime':
                answer1 = 700000
            elif genre == 'Animation':
                answer1 = 800000
            elif genre == 'Science Fiction':
                answer1 = 900000
            elif genre == 'Family':
                answer1 = 1000000
            elif genre == 'Drama':
                answer1 = 1100000
            elif genre == 'Western':
                answer1 = 1200000
            else:
                answer1 = 1300000

            # question 2
            if int(row[4]) < 100:
                answer2 = 100
            else:
                answer2 = 200

            # question 3
            if float(row[3]) >= 8.0 and float(row[3]) <= 10.0:
                answer3 = 1000
            elif float(row[3]) >= 5.0 and float(row[3]) <= 7.9:
                answer3 = 2000
            else:
                answer3 = 3000

            # question 4
            if row[0] == 'en':
                answer4 = 10000
            else:
                answer4 = 20000

            # question 5
            if row[2][:4] >= '2021':
                answer5 = 1
            elif row[2][:4] >= '2016' and row[2][:4] <= '2020':
                answer5 = 2
            else:
                answer5 = 3

            movie_scores[row[1]] = answer1 + answer2 + answer3 + answer4 + answer5
    return movie_scores
