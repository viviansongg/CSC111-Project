import tkinter as tk
from tkinter import *
import random
import moviegraph
import calculate_score
import main_block_2

# creates main root window and configure ideal size
main = tk.Tk()
main.geometry('500x700')
main.config(bg='thistle')
main.maxsize(500, 700)

frame = Frame(main)
# create a button
button_one = tk.Label(frame, text='Welcome to MovieFinder! \n'
                              'MovieFinder is an interactive program that will recommend a movie for you to watch \n'
                              'according to your unique taste! Answer some questions below and click done when you \n'
                              'have finalized your choices.')
button_one.pack()
frame.pack(padx=5, pady=5)
# create the frame where the questions, choices and movie recommendation will be displayed
frame1 = Frame(main)
frame1.pack(padx=5, pady=5)

# Question 1:
tk.Label(frame1, text='What genre of movie do you want to watch? Select one from the box below.').pack(anchor='w')
# Choices for question 1
options = ['Romance', 'Comedy', 'Action', 'Horror', 'Thriller', 'Adventure', 'Crime', 'Animation',
           'Science Fiction', 'Family', 'Drama', 'Western', 'Skip']
# stores the option that the user pressed on as a variable to be later used in choice_q_1
choice = StringVar()
drop_box = OptionMenu(frame1, choice, *options)


# based on the user choice in question 1, this function assigns a unique integer value to each option
def choice_q_1(answer: str) -> int:
    """Takes the string value for the choice the user made and turns it into a unique integer."""
    if answer == 'Romance':
        return 100000
    elif answer == 'Comedy':
        return 200000
    elif answer == 'Action':
        return 300000
    elif answer == 'Horror':
        return 400000
    elif answer == 'Thriller':
        return 500000
    elif answer == 'Adventure':
        return 600000
    elif answer == 'Crime':
        return 700000
    elif answer == 'Animation':
        return 800000
    elif answer == 'Science Fiction':
        return 900000
    elif answer == 'Family':
        return 1000000
    elif answer == 'Drama':
        return 1100000
    elif answer == 'Western':
        return 1200000
    elif answer == 'Fantasy':
        return 1300000
    else:
        lst_0 = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 100000, 1100000, 1200000,
                 1300000]
        return random.choice(lst_0)


drop_box.pack(anchor='w')

# store the choice that the user made as a variable to be used in the choice_q_2 function
choice_q_2 = StringVar()
choice_q_2.set('< 1h 40 min')
# Question 2:
tk.Label(frame1, text='Do you have a preference for the length of the movie?').pack(anchor='w')
# Choices for question 2
tk.Radiobutton(frame1, text='< 1h 40 min', variable=choice_q_2, value='< 1h 40 min').pack(anchor='w')
tk.Radiobutton(frame1, text='>= 1h 40 min', variable=choice_q_2, value='>= 1h 40 min').pack(anchor='w')
tk.Radiobutton(frame1, text='Skip', variable=choice_q_2, value='Skip').pack(anchor='w')


# function to assign a unique variable depending on which option the user chose for question 2
def choices_q_2(answer: str) -> int:
    """Takes the string value for the choice the user made and turns it into a unique integer."""
    if answer == '< 1h 40 min':
        return 100
    elif answer == '>= 1h 40 min':
        return 200
    else:
        lst = [100, 200]
        return random.choice(lst)


# store the choice that the user made for question 3 as a variable to be used later in the choice_q_3 function.
choice_q_3 = StringVar()
choice_q_3.set('High: 8-10')
# Question 3
tk.Label(frame1, text='Do you have a preference for the rating of the movie?').pack(anchor='w')
# Options for question 3
tk.Radiobutton(frame1, text='High: 8.0-10.0', variable=choice_q_3, value='High: 8.0-10.0').pack(anchor='w')
tk.Radiobutton(frame1, text='Mediocre: 5.0-7.9', variable=choice_q_3, value='Mediocre: 5.0-7.9').pack(anchor='w')
tk.Radiobutton(frame1, text='Low: 1.0-4.9', variable=choice_q_3, value='Low: 1.0-4.9').pack(anchor='w')
tk.Radiobutton(frame1, text='Skip', variable=choice_q_3, value='Skip').pack(anchor='w')


# function to assign a unique variable depending on which option the user chose for question 3
def choices_q_3(answer: str) -> int:
    """Takes the string value for the choice the user made and turns it into a unique integer."""
    if answer == 'High: 8.0-10.0':
        return 1000
    elif answer == 'Mediocre: 5.0-7.9':
        return 2000
    elif answer == 'Low: 1.0-4.9':
        return 3000
    else:
        lst_1 = [1000, 2000, 3000]
        return random.choice(lst_1)


# Question 4
choice_q_4 = StringVar()
choice_q_4.set('English')
tk.Label(frame1, text='What language do you want the movie to be in?').pack(anchor='w')
choices = ['English', 'Another Language', 'Skip']
tk.Radiobutton(frame1, text='English', variable=choice_q_4, value='English').pack(anchor='w')
tk.Radiobutton(frame1, text='Another Language', variable=choice_q_4, value='Another Language').pack(anchor='w')
tk.Radiobutton(frame1, text='Skip', variable=choice_q_4, value='Skip').pack(anchor='w')


def choices_q_4(answer: str) -> int:
    """Takes the string value for the choice the user made and turns it into a unique integer."""
    if answer == 'English':
        return 10000
    elif answer == 'Another Language':
        return 20000
    else:
        lst_2 = [10000, 20000]
        return random.choice(lst_2)


# Question 5
choice_q_5 = StringVar()
choice_q_5.set('>=2021')
tk.Label(frame1, text='Do you have a preference for what year the movie should be released?').pack(anchor='w')
tk.Radiobutton(frame1, text='>=2021', variable=choice_q_5, value='>=2021').pack(anchor='w')
tk.Radiobutton(frame1, text='2016-2020', variable=choice_q_5, value='2016-2020').pack(anchor='w')
tk.Radiobutton(frame1, text='<2016', variable=choice_q_5, value='<2016').pack(anchor='w')
tk.Radiobutton(frame1, text='Skip', variable=choice_q_5, value='Skip').pack(anchor='w')


def choices_q_5(answer: str) -> int:
    """Takes the string value for the choice the user made and turns it into a unique integer."""
    if answer == '>=2021':
        return 1
    elif answer == '2016-2020':
        return 2
    elif answer == '<2016':
        return 3
    else:
        lst_3 = [1, 2, 3]
        return random.choice(lst_3)


def quit_window():
    """After the user presses this button, the interactive window will close."""
    main.destroy()


def clicked():
    """When the done button is clicked switch the text to loading."""
    movie_scores = calculate_score.calculate_score1('movies_first_100.csv')
    initial_network = moviegraph.MovieNetwork()
    movie_network = moviegraph.movienetworkcreate(initial_network, movie_scores)
    score = choice_q_1(choice.get()) + choices_q_2(choice_q_2.get()) + choices_q_3(choice_q_3.get()) \
            + choices_q_4(choice_q_4.get()) + choices_q_5(choice_q_5.get())
    print(score)
    movie_to_watch = main_block_2.watch_next(movie_network.movies, score)
    text_label = tk.Label(frame1, text='The movie you should watch next is:')
    text_label.pack(padx=5, pady=5)
    movie_recommender = tk.Label(frame1, text=movie_to_watch)
    movie_recommender.pack(padx=5, pady=5)
    quit_when_done.config(text='QUIT', command=quit_window)


quit_when_done = Button(main, text='DONE', command=clicked)
quit_when_done.pack(padx=5, pady=5)

# loop over python code
main.mainloop()
