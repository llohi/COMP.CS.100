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
import random
from tkinter import *


#  representation of the main window
class UserInterface:

    def __init__(self):

        #  create root window with size and title
        self.root = Tk()
        self.root.geometry('1030x720')
        self.root.title('Who Wants to Be a Millionaire?')

        #  set background
        background = Label(bg='#FFF', width=1280, height=720)
        background.place(x=0, y=0)

        #  set header
        self.header = Label(text='Who Wants to Be a Millionaire?', bg='#FFF')
        self.header.config(font=('Serif', 30))

        #  frame for prizes
        self.left_frame = Frame(self.root, width=175, height=520, bg='#FFF', bd=5, relief=RIDGE)

        #  frame for questions and answers:
        #   - START button
        #   - frame for question string
        self.middle_frame = Frame(self.root, width=600, height=520, bg='#FFF', bd=5, relief=RIDGE)
        self.start_button = Button(self.middle_frame, text='START', bg='green', fg='white', padx=20, pady=20, bd=5, relief=RIDGE, command=self.ask_questions)
        self.question_frame = Frame(self.middle_frame, width=500, height=100, bg='#FFF')

        #  frame for right sidebar:
        #   - prize count
        #   - operators (50/50, ask the audience)
        #   - QUIT button
        self.right_frame = Frame(self.root, width=100, height=520, bg='#FFF', bd=5, relief=RIDGE)
        self.count = 0
        self.count_label = Label(self.right_frame, text=f'CORRECT:\n{self.count}', bg='#FFF')
        self.ff = Button(self.right_frame, text='50/50', padx=27, pady=15)
        self.ask = Button(self.right_frame, text='ASK THE\nAUDIENCE', pady=10)

        #  QUIT button
        self.quit = Button(self.right_frame, text='QUIT', bg='red', fg='white', padx=26, pady=15, bd=5, relief=RIDGE, command=self.root.quit)


        #  grid system:
        #                       HEADER
        #  LEFT (prizes)    MIDDLE (questions)    RIGHT(buttons)

        self.header.grid(row=0, column=0, columnspan=3, pady=20)

        #  LEFT

        self.left_frame.grid(row=1, column=0, padx=20, pady=20)
        self.left_frame.grid_propagate(0)  # freeze size of frame
        # question/prize
        Label(self.left_frame, text='QUESTION', bg='#FFF').grid(row=0, column=0, padx=3, pady=10)
        Label(self.left_frame, text='PRIZE', bg='#FFF').grid(row=0, column=1, padx=3, pady=10)
        # label prizes
        i = 1
        for p in PRIZES:
            Label(self.left_frame, text=p, bg='#FFF').grid(row=i, column=0, pady=9)
            Label(self.left_frame, text=f'{PRIZES[p]} $', bg='#FFF').grid(row=i, column=1)
            i += 1

        #  MIDDLE

        self.middle_frame.grid(row=1, column=1, padx=20, pady=20)
        self.middle_frame.grid_propagate(0)  # freeze size of frame
        self.start_button.grid(row=1, column=0, padx=250, pady=50)
        self.question_frame.grid(row=0, column=0, padx=50, pady=20)
        self.question_frame.grid_propagate(0)

        #  RIGHT

        self.right_frame.grid(row=1, column=2, padx=20, pady=100)
        self.count_label.grid(row=0, column=0, pady=10)
        self.ff.grid(row=1, column=0, pady=10)
        self.ask.grid(row=2, column=0, pady=10)
        self.quit.grid(row=3, column=0, pady=10)


    #  initialize event loop
    def start(self):

        self.root.mainloop()

    #  ask questions
    #  if answer is incorrect  ->  break loop and ask for restart
    def ask_questions(self):

        #  remove button
        self.start_button.grid_forget()

        self.answer_frame = Frame(self.middle_frame, width=536, height=265, bg='#FFF')
        self.answer_frame.grid(row=1, column=0, padx=23)
        self.answer_frame.grid_propagate(0)

        #  list of all questions
        questions = []
        for q in QA:
            questions.append(q)

        # ask 12 questions
        x = 0
        while x < 1:

            question = random.choice(list(questions))
            questions.remove(question)  # dont ask question again

            # answers for the question
            answers = []
            for answer in QA[question]:
                answers.append(QA[question][answer])

            random.shuffle(answers)

            print(answers)

            # grid the question
            msg = Message(self.question_frame, text=question, width=490, bg='#FFF', anchor='center', justify='center')
            msg.config(font=('Helvetica', 15))
            msg.grid(row=0, column=0)

            # grid the answers
            Button(self.answer_frame, text=answers[0], width=30, height=7).grid(row=0, column=0)
            Button(self.answer_frame, text=answers[1], width=30, height=7).grid(row=0, column=1)
            Button(self.answer_frame, text=answers[2], width=30, height=7).grid(row=1, column=0)
            Button(self.answer_frame, text=answers[3], width=30, height=7).grid(row=1, column=1)

            x += 1


#  representation of a question
class Question:

    def __init__(self, question, correct, false_1, false_2, false_3):

        self.question = question
        self.correct = correct
        self.false_1 = false_1
        self.false_2 = false_2
        self.false_3 = false_3


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
QA = {}
file = open(f'{path}/questions.csv')

for row in file:
    row = row.rstrip().split(';')

    q = Question(row[0], row[1], row[2], row[3], row[4])
    QA[row[0]] = {'true': q.correct, 'false_1': q.false_1, 'false_2': q.false_2, 'false_3': q.false_3}

def main():

    ui = UserInterface()
    ui.start()

if __name__ == '__main__':
    main()
