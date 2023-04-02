"""Computing Scores for Movies
"""

def calculate_score(movie_file: str) -> dict:
    """Returns a dictionary mapping each movie in the csv file to its associated score.
    """
    movie_scores = {}
    with open(movie_file) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            # question 1
            genre = row[5]
            genre = genre.strip("[']")
            answer1 = choices_q_1(genre)

            # question 2
            if int(row[4]) < 100:
                answer2 = 100
            elif int(row[4]) >= 100:
                answer2 = 200
            else:
                answer2 = 300

            # question 3
            if float(row[3]) >= 8.0 and float(row[3]) <= 10.0:
                answer3 = 1000
            elif float(row[3]) >= 5.0 and float(row[3]) <= 7.9:
                answer3 = 2000
            elif float(row[3]) >= 1.0 and float(row[3]) <= 4.9:
                answer3 = 3000
            else:
                answer3 = 4000

            # question 4
            if row[0] == 'en':
                answer4 = 10000
            else:
                answer4 = 2000

            # question 5
            if row[2][:4] >= '2021':
                answer5 = 100000
            elif row[2][:4] >= '2016' and row[2][:4] <= '2020':
                answer5 = 200000
            elif row[2][:4] < '2016':
                answer5 = 300000
            else:
                answer5 = 400000
            movie_scores[row[1]] = answer1 + answer2 + answer3 + answer4 + answer5
    return movie_scores
