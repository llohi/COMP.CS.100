"""
COMP.CS.100 Who Wants to Be a Millionaire?
Tekijä: Joose Lohi
Opiskelijanumero: 050800360

This program simulates the game show known as Who Wants to Be a Millionaire.
The player is given a question and four options. If the answer is correct,
the prize increases and the player moves on to the next question. If the answer is incorrect,
the game ends. To win, the player must answer all 12 questions correctly.
"""


import os
import random
from tkinter import *

#  shortcut to directory with files
path = __file__.strip(os.path.basename(__file__))

#  string for the rules of the game
RULES = """
    Welcome to the game!

    The rules are simple:
        - choose the correct answer and your prize gets bigger
        - answer all 12 questions correctly to win 1 000 000$

    Good Luck!
    """
#  dictionary for prizes
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


#  representation of the user interface
class UserInterface:

    #  initialize all frames and variables of the user interface here
    def __init__(self):

        #  create root window with size and title
        self.root = Tk()
        self.root.geometry('1010x640')
        self.root.title('Who Wants to Be a Millionaire?')
        #  set background
        background = Label(bg='#FFF', width=1280, height=720)
        background.place(x=0, y=0)

        #  initialize variables
        self.questions = []
        self.question = ''

        #  set header
        self.header = Label(text='Who Wants to Be a Millionaire?', bg='#FFF')
        self.header.config(font=('Serif', 30))

        #  set left frame
        self.left_frame = Frame(self.root, width=175, height=520, bg='#FFF', bd=5, relief=RIDGE)

        #  set middle frame:  rules, START button, frame for question and frame for answers
        self.middle_frame = Frame(self.root, width=600, height=520, bg='#FFF', bd=5, relief=RIDGE)
        self.rules = Message(self.middle_frame, text=RULES, font=('Helvetica', 15), bg='#FFF', width=560, padx=20, pady=20)
        self.start_button = Button(self.middle_frame, text='START', bg='green', fg='white', padx=20, pady=20, bd=5, relief=RIDGE, command=self.start_with_skip)
        self.question_frame = Frame(self.middle_frame, width=500, height=100, bg='#FFF')
        self.answer_frame = Frame(self.middle_frame, width=536, height=265, bg='#FFF')

        #  set right frame:  prize count, SKIP button and QUIT button
        self.right_frame = Frame(self.root, width=100, height=520, bg='#FFF', bd=5, relief=RIDGE)
        self.count = 0
        self.count_label = Label(self.right_frame, text=f'PRIZE:\n0$', bg='#FFF')
        self.skip = Button(self.right_frame, text='SKIP', bg='#0039E6', fg='#FFF', padx=25, pady=15, bd=5, relief=RIDGE, state=DISABLED, command=self.skip_question)
        self.quit = Button(self.right_frame, text='QUIT', bg='red', fg='#FFF', padx=26, pady=15, bd=5, relief=RIDGE, command=self.root.quit)

    #  initialize event loop
    def start(self):

        self.questions = list(QA)
        self.grid_ui()
        self.root.mainloop()

    #  initialize grid system
    def grid_ui(self):
        #                       HEADER
        #  LEFT FRAME        MIDDLE FRAME        RIGHT FRAME

        self.header.grid(row=0, column=0, columnspan=3, pady=10)

        self.left_frame.grid(row=1, column=0, padx=20, pady=20)
        self.left_frame.grid_propagate(0)  # freeze size of frame
        # question/prize
        Label(self.left_frame, text='QUESTION', bg='#FFF').grid(row=0, column=0, padx=3, pady=10)
        Label(self.left_frame, text='PRIZE', bg='#FFF').grid(row=0, column=1, padx=3, pady=10)
        # label prizes
        i = 1
        for num in PRIZES:
            Label(self.left_frame, text=num, bg='#FFF').grid(row=i, column=0, pady=9)
            Label(self.left_frame, text=f'{PRIZES[num]} $', bg='#FFF').grid(row=i, column=1)
            i += 1

        self.middle_frame.grid(row=1, column=1, padx=20, pady=20)
        self.middle_frame.grid_propagate(0)  # freeze size of frame
        self.rules.grid(row=0, column=0)
        self.start_button.grid(row=1, column=0, padx=250, pady=20)

        self.right_frame.grid(row=1, column=2, padx=20, pady=100)
        self.count_label.grid(row=0, column=0, pady=10)
        self.skip.grid(row=1, column=0, pady=10)
        self.quit.grid(row=2, column=0, pady=10)

    #  the purpose of this function is to start the
    #  game with the skip button enabled
    def start_with_skip(self):

        #  enable skip button
        self.skip.config(state = NORMAL)
        self.ask_questions()


    #  ask question and create interactive buttons for answers
    def ask_questions(self):

        #  clear screen
        self.rules.grid_forget()
        self.start_button.grid_forget()

        #  grid frames and freeze their size
        self.question_frame.grid(row=0, column=0, padx=50, pady=20)
        self.answer_frame.grid(row=1, column=0, padx=23)
        self.question_frame.grid_propagate(0)
        self.answer_frame.grid_propagate(0)

        #  grid the question inside its frame
        self.question = random.choice(self.questions)
        q = Message(self.question_frame, text=self.question, width=490, bg='#FFF', anchor='center', justify='center', font=('Helvetica', 16))
        q.grid(row=0, column=0)

        #  get answers from global dictionary QA
        answers = QA[self.question]

        #  shuffle answers
        items = list(answers.items())
        random.shuffle(items)
        answers = dict(items)

        #  grid the answers:
        #      A    B
        #      C    D
        Button(self.answer_frame, text=list(answers)[0], width=30, height=7, command=lambda: self.click_answer(answers[list(answers)[0]], q)).grid(row=0, column=0)
        Button(self.answer_frame, text=list(answers)[1], width=30, height=7, command=lambda: self.click_answer(answers[list(answers)[1]], q)).grid(row=0, column=1)
        Button(self.answer_frame, text=list(answers)[2], width=30, height=7, command=lambda: self.click_answer(answers[list(answers)[2]], q)).grid(row=1, column=0)
        Button(self.answer_frame, text=list(answers)[3], width=30, height=7, command=lambda: self.click_answer(answers[list(answers)[3]], q)).grid(row=1, column=1)


    #  react to the answer button according to
    #  its assigned boolean value
    def click_answer(self, run, q):

        #  if correct
        if run == True:

            #  if not last question
            if self.count < 11:
                q.destroy()  # clear message from screen
                self.questions.remove(self.question)  # make sure same question not asked again
                self.count += 1
                self.count_label.config(text = f'PRIZE:\n{PRIZES[list(PRIZES)[self.count - 1]]}$')  # udate prize text
                self.ask_questions()  # go again

            #  user answered all questions correctly
            else:
                #  clear the screen
                q.destroy()
                self.question_frame.grid_forget()
                self.answer_frame.grid_forget()

                #  disable skip button
                self.skip.config(state = DISABLED)

                self.count_label.config(text = f'PRIZE:\n{PRIZES[list(PRIZES)[self.count - 1]]}$')

                end_label = Label(self.middle_frame, text='Congratulations, you have won 1 000 000$!\nWant to play again?', bg='#FFF', font=('Helvetica', 16))
                end_label.grid(row=0, column=0, padx=80, pady=20)

                restart_button = Button(self.middle_frame, text='RESTART', command=lambda: self.restart(end_label, restart_button))
                restart_button.grid(row=1, column=0, pady=20)

        #  if incorrect
        else:

            #  clear the screen
            q.destroy()
            self.question_frame.grid_forget()
            self.answer_frame.grid_forget()

            #  disable skip button
            self.skip.config(state = DISABLED)

            if self.count > 0:  # player got atleast one correct answer
                end_msg = f'Wrong answer, you won {PRIZES[list(PRIZES)[self.count - 1]]}$, good luck next time !'

            else:
                end_msg = 'Wrong answer. You won nothing, good luck next time!'

            #  grid ending message
            end_label = Label(self.middle_frame, text=end_msg, bg='#FFF', font=('Helvetica', 16))
            end_label.grid(row=0, column=0, padx=40, pady=20)

            #  grid restart button
            restart_button = Button(self.middle_frame, text='RESTART', command=lambda: self.restart(end_label, restart_button))
            restart_button.grid(row=1, column=0, pady=20)

    #  skip current question and move to next one
    def skip_question(self):

        #  disable the skip button
        self.skip.config(state = DISABLED)

        #  clear frames
        for widget in self.question_frame.winfo_children():
            widget.grid_forget()

        for widget in self.answer_frame.winfo_children():
            widget.grid_forget()

        #  remove question from list
        self.questions.remove(self.question)

        #  continue
        self.ask_questions()


    #  function initialized if player wants to go again
    #  clear screen  ->  update class attributes  ->  start asking questions
    def restart(self, label, button):

        #  clear screen
        label.destroy()
        button.destroy()

        #  update all questions back to list and zero counter
        self.questions = list(QA)
        self.count = 0
        self.count_label.config(text = f'PRIZE:\n0$')

        #  restart game with one skip
        self.start_with_skip()


def main():

    ui = UserInterface()
    ui.start()

if __name__ == '__main__':
    main()
