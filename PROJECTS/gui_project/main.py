"""
COMP.CS.100 Who Wants to Be a Millionaire?
Tekijä: Joose Lohi
Opiskelijanumero: 050800360

This program simulates the game show known as Who Wants to Be a Millionaire.
The player is given a question and four options (A, B, C and D). If the answer is correct,
the prize increases and the player moves on to the next question. If the answer is incorrect,
the game ends. To win, the player must answer all 12 questions correctly.
"""


import os
from tkinter import *


#  representation of the main window
class UserInterface:

    def __init__(self):

        #  create root window with size and title
        self.__root = Tk()
        self.__root.geometry('1280x720')
        self.__root.title('Who Wants to Be a Millionaire?')

        #  set background image
        self.__background_image = PhotoImage(file=f'{path}/background.png')
        self.__background_label = Label(self.__root, image=self.__background_image)
        self.__background_label.place(x=0, y=0, relwidth=1, relheight=1)

        #  frame for prizes                                520 / 13 = 20
        self.__prize_frame = Frame(self.__root, width=175, height=520, background='#ffffff', bd=5, relief=RIDGE)
        self.__prize_frame.grid(row=0, column=0, padx=50, pady=120)

        # question/prize
        Label(self.__prize_frame, text='QUESTION', background='#FFFFFF').grid(row=0, column=0, padx=10, pady=10)
        Label(self.__prize_frame, text='PRIZE', background='#FFFFFF').grid(row=0, column=1, padx=10, pady=10)
        # label prizes
        i = 1
        for p in PRIZES:
            Label(self.__prize_frame, text=p, background='#FFFFFF').grid(row=i, column=0, padx=10, pady=10)
            Label(self.__prize_frame, text=f'{PRIZES[p]} $', background='#FFFFFF').grid(row=i, column=1, padx=10, pady=10)
            i += 1


        #  frame for q&a
        self.__question_frame = Frame(self.__root, width=600, height=520, background='#ffffff', bd=5, relief=RIDGE)
        self.__question_frame.grid(row=0, column=1, padx=50, pady=120)


    #  initialize event loop
    def start(self):

        self.__root.mainloop()




#  shortcut to directory with files
#   - note: using os.getcwd() also works, but may cause errors if
#     program is not ran from the same directory as files
path = __file__.strip(os.path.basename(__file__))


# dict for prizes
PRIZES = {
    '1': '500', '2': '1 000', '3': '2 000', '4': '5 000',
    '5': '10 000', '6': '20 000', '7': '50 000', '8': '75 000',
    '9': '150 000', '10': '250 000', '11': '500 000', '12': '1 000 000'
    }

# dict for q&a
QUESTIONS = {}
file = open(f'{path}/questions.csv')

for row in file:
    row = row.rstrip().split(';')

    #   question           A       B       C       D
    QUESTIONS[row[0]] = [row[1], row[2], row[3], row[4]]

print(QUESTIONS)

def main():

    ui = UserInterface()
    ui.start()

if __name__ == '__main__':
    main()
