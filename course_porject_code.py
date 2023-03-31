import tkinter as tk
from tkinter import *

# creates main root window
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
frame1 = Frame(main)
frame1.pack(padx=5, pady=5)
# question 1
questions = ['What genre of movie do you want to watch?', 'Length of Movie?', 'Preference for rating of movie?',
             'What Language do you want the movie to be in?',
             'Do you have a preference for what year the movie should be released?']
answers = [['Romance', 'Comedy', 'Action', 'Horror', 'Thriller'], ['< 1h 40 min', '>= 1h 40 min'],
           ['High: 8-10', ' Mediocre: 5-7',  'Low: 1-4', 'No preference'], ['English', 'Japanese', 'Italian'],
           ['2021', '2016-2020', '<2016', 'Skip']]

# We use IntVar to keep track of the choice and number that the user chose so that we can later put this in a list

#frame2 = Frame(main)
#frame2.pack(padx=5, pady=5)
# Question 1:
tk.Label(frame1, text='What genre of movie do you want to watch? Select one from the box below.').pack(anchor='w')
# Choices for question 1
options = ['Romance', 'Comedy', 'Action', 'Horror', 'Thriller', 'Action', 'Skip']
choice = StringVar()
drop_box = OptionMenu(frame1, choice, *options)
drop_box.pack(anchor='w')

#frame3 = Frame(main)
#frame3.pack(padx=5, pady=5)
choice_q_2 = StringVar()
choice_q_2.set('< 1h 40 min')
# Question 2:
tk.Label(frame1, text='Do you have a preference for the length of the movie?').pack(anchor='w')
# Choices for question 2
tk.Radiobutton(frame1, text='< 1h 40 min', variable=choice_q_2, value='< 1h 40 min').pack(anchor='w')
tk.Radiobutton(frame1, text='>= 1h 40 min', variable=choice_q_2, value='>= 1h 40 min').pack(anchor='w')
tk.Radiobutton(frame1, text='Skip', variable=choice_q_2, value='Skip').pack(anchor='w')

#frame4 = Frame(main)
# Question 3:
choice_q_3 = StringVar()
choice_q_3.set('High: 8-10')
tk.Label(frame1, text='Do you have a preference for the rating of the movie?').pack(anchor='w')
tk.Radiobutton(frame1, text='High: 8-10', variable=choice_q_3, value='High: 8-10').pack(anchor='w')
tk.Radiobutton(frame1, text='Mediocre: 5-7', variable=choice_q_3, value='Mediocre: 5-7').pack(anchor='w')
tk.Radiobutton(frame1, text='Low: 1-4', variable=choice_q_3, value='Low: 1-4').pack(anchor='w')
tk.Radiobutton(frame1, text='Skip', variable=choice_q_3, value='Skip').pack(anchor='w')
#frame4.pack(padx=5, pady=5)

#frame5 = Frame(main)
# Question 4
tk.Label(frame1, text='What language do you want the movie to be in?').pack(anchor='w')
choices = ['English', 'Japanese', 'Italian', 'French', 'No Preference', 'Skip']
choice_q_4 = StringVar()
drop_box_2 = OptionMenu(frame1, choice_q_4, *choices)
drop_box_2.pack(anchor='w')
#frame5.pack(padx=5, pady=5)

#frame6 = Frame(main)
# Question 5
choice_q_5 = StringVar()
choice_q_5.set('2021')
tk.Label(frame1, text='Do you have a preference for what year the movie should be released?').pack(anchor='w')
tk.Radiobutton(frame1, text='2021', variable=choice_q_5, value='2021').pack(anchor='w')
tk.Radiobutton(frame1, text='2016-2020', variable=choice_q_5, value='2016-2020').pack(anchor='w')
tk.Radiobutton(frame1, text='<2016', variable=choice_q_5, value='<2016').pack(anchor='w')
tk.Radiobutton(frame1, text='Skip', variable=choice_q_5, value='Skip').pack(anchor='w')
#frame6.pack(padx=5, pady=5)
# Question 6

def clicked():
    """When the done button is clicked switch the text to loading."""
    quit_when_done.config(text='LOADING...')
    print([choice.get()] + [choice_q_2.get()] + [choice_q_3.get()] + [choice_q_4.get()]
          + [choice_q_5.get()])

quit_when_done = Button(main, text='DONE', command=clicked)
quit_when_done.pack(padx=5, pady=5)

import csv
# function to sort through the words in the plot
def word_tally(csv_lst: str) -> dict[str, int]:
    """Returns a tally for each word in the plot of each movie"""
    # index 9
    dict_so_far = {}
    lst = csv_lst.split()
    for word in lst:
        if word not in dict_so_far:
            dict_so_far[word] = 1
        else:
            dict_so_far[word] = dict_so_far[word] + 1
    return dict_so_far


# loop over python code
main.mainloop()
