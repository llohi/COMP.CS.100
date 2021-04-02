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

        #  if run == False, break program
        self.run = True
        self.questions = []
        self.question = ''

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
        #   - frame for answers
        self.middle_frame = Frame(self.root, width=600, height=520, bg='#FFF', bd=5, relief=RIDGE)
        self.start_button = Button(self.middle_frame, text='START', bg='green', fg='white', padx=20, pady=20, bd=5, relief=RIDGE, command=self.ask_questions)
        self.question_frame = Frame(self.middle_frame, width=500, height=100, bg='#FFF')
        self.answer_frame = Frame(self.middle_frame, width=536, height=265, bg='#FFF')

        #  frame for right sidebar:
        #   - prize count
        #   - operators (50/50, ask the audience)
        #   - QUIT button
        self.right_frame = Frame(self.root, width=100, height=520, bg='#FFF', bd=5, relief=RIDGE)
        self.count = 0
        self.count_label = Label(self.right_frame, text=f'PRIZE:\n0$', bg='#FFF')
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

        #  RIGHT

        self.right_frame.grid(row=1, column=2, padx=20, pady=100)
        self.count_label.grid(row=0, column=0, pady=10)
        self.ff.grid(row=1, column=0, pady=10)
        self.ask.grid(row=2, column=0, pady=10)
        self.quit.grid(row=3, column=0, pady=10)


    #  initialize event loop
    def start(self):

        self.questions = list(QA)
        self.root.mainloop()

    #  ask questions
    #  if answer is incorrect  ->  break loop and ask for restart
    def ask_questions(self):

        #  remove button
        self.start_button.grid_forget()

        #  grid question and answer frames
        self.question_frame.grid(row=0, column=0, padx=50, pady=20)
        self.question_frame.grid_propagate(0)
        self.answer_frame.grid(row=1, column=0, padx=23)
        self.answer_frame.grid_propagate(0)

        # grid the question
        self.question = random.choice(self.questions)
        msg = Message(self.question_frame, text=self.question, width=490, bg='#FFF', anchor='center', justify='center', font=('Helvetica', 16))
        msg.grid(row=0, column=0)

        # answers for the question
        answers = QA[self.question]

        # shuffle answers
        items = list(answers.items())
        random.shuffle(items)
        answers = dict(items)

        #  grid the answers:
        #      A    B
        #      C    D
        Button(self.answer_frame, text=list(answers)[0], width=30, height=7, command=lambda: self.click_answer(answers[list(answers)[0]], msg)).grid(row=0, column=0)
        Button(self.answer_frame, text=list(answers)[1], width=30, height=7, command=lambda: self.click_answer(answers[list(answers)[1]], msg)).grid(row=0, column=1)
        Button(self.answer_frame, text=list(answers)[2], width=30, height=7, command=lambda: self.click_answer(answers[list(answers)[2]], msg)).grid(row=1, column=0)
        Button(self.answer_frame, text=list(answers)[3], width=30, height=7, command=lambda: self.click_answer(answers[list(answers)[3]], msg)).grid(row=1, column=1)


    def click_answer(self, run, msg):

        #  if correct
        if run == True:

            if self.count < 11:
                msg.destroy()  # clear message from screen
                self.questions.remove(self.question)  # make sure same question not asked again
                self.count += 1
                self.count_label.config(text = f'PRIZE:\n{PRIZES[list(PRIZES)[self.count - 1]]}$')  # udate prize text
                self.ask_questions()  # go again

            #  user answered all questions correctly
            else:
                #  clear the screen
                msg.destroy()
                self.question_frame.grid_forget()
                self.answer_frame.grid_forget()

                self.count_label.config(text = f'PRIZE:\n{PRIZES[list(PRIZES)[self.count - 1]]}$')

                end_label = Label(self.middle_frame, text='Congratulations, you have won 1 000 000$!\nWant to play again?', background='#FFF', font=('Helvetica', 16))
                end_label.grid(row=0, column=0, padx=80, pady=20)

                restart_button = Button(self.middle_frame, text='RESTART', command=lambda: self.restart(end_label, restart_button))
                restart_button.grid(row=1, column=0, pady=20)

        #  if incorrect
        else:

            #  clear the screen
            msg.destroy()
            self.question_frame.grid_forget()
            self.answer_frame.grid_forget()

            if self.count > 0:
                end_msg = f'Wrong answer, you won {PRIZES[list(PRIZES)[self.count - 1]]}$, good luck next time !'

            else:
                end_msg = 'Wrong answer. You won nothing, good luck next time!'

            #  label ending message
            end_label = Label(self.middle_frame, text=end_msg, background='#FFF', font=('Helvetica', 16))
            end_label.grid(row=0, column=0, padx=40, pady=20)

            #  label restart button
            restart_button = Button(self.middle_frame, text='RESTART', command=lambda: self.restart(end_label, restart_button))
            restart_button.grid(row=1, column=0, pady=20)


    def restart(self, label, button):

        #  clear screen
        label.destroy()
        button.destroy()

        #  update all questions back to list and zero counter
        self.questions = list(QA)
        self.count = 0
        self.count_label.config(text = f'PRIZE:\n0$')

        #  restart game
        self.ask_questions()


#  shortcut to directory with files
#   - note: using os.getcwd() also works, but may cause errors if
#     program is not ran from the same directory as files
path = __file__.strip(os.path.basename(__file__))

# dictionary for prizes
PRIZES = {
    '1': '500', '2': '1 000', '3': '2 000', '4': '5 000',
    '5': '10 000', '6': '20 000', '7': '50 000', '8': '75 000',
    '9': '150 000', '10': '250 000', '11': '500 000', '12': '1 000 000'
    }

#  create dictionary for questions and answers
#  {'question_1?': {'answer_1': True, 'answer_2': False, 'answer_3': False, 'answer_4': False}}
QA = {}
file = open(f'{path}/questions.csv')

for row in file:
    row = row.rstrip().split(';')
    QA[row[0]] = {row[1]: True, row[2]: False, row[3]: False, row[4]: False}

def main():

    ui = UserInterface()
    ui.start()

if __name__ == '__main__':
    main()
