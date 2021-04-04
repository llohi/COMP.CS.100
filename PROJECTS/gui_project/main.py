"""
COMP.CS.100 gui_project: Who Wants to Be a Millionaire?
Tekijä: Joose Lohi
Opiskelijanumero: 050800360

This  program  simulates the game show known as Who Wants to
Be  a  Millionaire.  The player is given a question and four
options. If  the answer is correct, the prize  increases and
the  player moves on to the next  question. If the answer is
incorrect, the game ends. The player is also given one  skip
and they may cash out at any  point in the game. To win, the
player must answer all 12  questions correctly.

Please, to avoid errors keep the file 'questions.csv' in the
same directory as this file.
"""

import os
import random
from tkinter import *

#  shortcut to directory with files
PATH = __file__.strip(os.path.basename(__file__))

#  string for the rules of the game
RULES = """
    Welcome to the game!

    The rules are simple:

     * choose the correct answer and your prize gets bigger

     * 1 000$ and 50 000$ are guaranteed if you reach them

     * you may cash out at any point

     * you have one skip

     * answer all 12 questions correctly to win 1 000 000$

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
file = open(f'{PATH}/questions.csv')

for row in file:
    row = row.rstrip().split(';')
    QA[row[0]] = {row[1]: True, row[2]: False, row[3]: False, row[4]: False}


#  chart with prize info
class LeftFrame:

    #  'root' variable is the main window
    def __init__(self, root):

        #  create
        self.frame = Frame(root, width=175, height=520, bg='#FFF', bd=5, relief=RIDGE)

        # header 'QUESTION    PRIZE'
        Label(self.frame, text='QUESTION    PRIZE', bg='#FFF').grid(row=0, padx=3, pady=10)

        # create labels for prizes
        prizes = {}
        for num in range(1, 13):
            prizes[f'prize_{num}'] = Label(self.frame, text='{: ^{width}}'.format(f' {num}:   {PRIZES[str(num)]} ', width=19), bg='#FFF', width=19)
            prizes[f'prize_{num}'].grid(row=num, padx=5, pady=9)

        prizes['prize_2'].config(bg = '#FFE6B3')
        prizes['prize_7'].config(bg = '#FFE6B3')
        prizes['prize_12'].config(bg = '#FFBB33')


#  1) print rules and display start button
#  2) show question and answers
class MiddleFrame:

    def __init__(self, root, start_function):

        #  create
        self.frame = Frame(root, width=600, height=520, bg='#FFF', bd=5, relief=RIDGE)
        self.rules = Message(self.frame, text=RULES, font=('Helvetica', 13), bg='#FFF', width=560, padx=20, pady=20)
        self.start_button = Button(self.frame, text='START', bg='green', fg='white', padx=20, pady=20, bd=5, relief=RIDGE, command=start_function)
        self.question_frame = Frame(self.frame, width=500, height=100, bg='#FFF')
        self.answer_frame = Frame(self.frame, width=536, height=265, bg='#FFF')

        #  grid
        self.rules.grid(row=0)
        self.start_button.grid(row=1, padx=230, pady=10)


#  show three things: prize count, SKIP button and QUIT button
class RightFrame:

    def __init__(self, root, skip_function, cash_out_function):

        #  create
        self.frame = Frame(root, width=100, height=520, bg='#FFF', bd=5, relief=RIDGE)
        self.count = 0
        self.count_label = Label(self.frame, text=f'PRIZE:\n0$', bg='#FFF')
        self.skip = Button(self.frame, text='SKIP', bg='#0039E6', fg='#FFF', padx=25, pady=15, bd=5, relief=RIDGE, state=DISABLED, command=skip_function)
        self.out = Button(self.frame, text='CASH\nOUT', bg='#FFC34D', padx=25, pady=5, bd=5, relief=RIDGE, state=DISABLED, command=cash_out_function)
        self.quit = Button(self.frame, text='QUIT', bg='red', fg='white', padx=26, pady=15, bd=5, relief=RIDGE, command=root.quit)

        #  grid
        self.count_label.grid(row=0, pady=10)
        self.skip.grid(row=1, pady=10)
        self.out.grid(row=2, pady=10)
        self.quit.grid(row=3, pady=10)

class UserInterface:

    def __init__(self):

        #  create main window with resolution 1010x640, title and white background
        self.root = Tk()
        self.root.geometry('1010x640')
        self.root.title('Who Wants to Be a Millionaire?')
        Label(bg='#FFF', width = 1010, height=640).place(x=0, y=0)

        #  initialize variables used to store questions
        self.questions = []
        self.question = ''

        #  header displays the title
        self.header = Label(text='Who Wants to Be a Millionaire?', bg='#FFF', font=('Serif', 30))

        #  left frame
        self.left = LeftFrame(self.root)

        #  middle frame
        self.middle = MiddleFrame(self.root, self.start_with_skip)

        #  right frame
        self.right = RightFrame(self.root, self.skip_question, self.cash_out)

    #  generate question list
    #  initialize event loop
    def start(self):

        self.questions = list(QA)
        self.grid_ui()
        self.root.mainloop()


    #  grid all class attributes
    #  notice many attributes have been pre-gridded in child classes
    def grid_ui(self):

        self.header.grid(row=0, columnspan=3, pady=10)

        self.left.frame.grid(row=1, column=0, padx=20, pady=20)
        self.left.frame.grid_propagate(0)  # freeze size of frame

        self.middle.frame.grid(row=1, column=1, padx=20, pady=20)
        self.middle.frame.grid_propagate(0)

        self.right.frame.grid(row=1, column=2, padx=20, pady=100)


    #  the purpose of this function is to start the
    #  game with the skip button enabled
    def start_with_skip(self):

        #  enable skip button
        self.right.skip.config(state = NORMAL)
        self.ask_questions()


    #  ask questions and create interactive buttons for answers
    def ask_questions(self):

        if self.right.count > 0:
            #  enable cashout button
            self.right.out.config(state = NORMAL)
        else:
            pass

        #  assign easier names for readability
        middle_frame = self.middle.frame
        question_frame = self.middle.question_frame
        answer_frame = self.middle.answer_frame

        #  clear screen
        self.middle.rules.grid_forget()
        self.middle.start_button.grid_forget()

        #  grid frames and freeze their size
        question_frame.grid(row=0, padx=50, pady=20)
        answer_frame.grid(row=1, padx=23)
        question_frame.grid_propagate(0)
        answer_frame.grid_propagate(0)

        #  grid the question inside its frame
        self.question = random.choice(self.questions)
        question_text = Message(question_frame, text=self.question, width=490, bg='#FFF', anchor='center', justify='center', font=('Helvetica', 16))
        question_text.pack()

        #  get answers from global dictionary QA
        answers = QA[self.question]

        #  shuffle answers
        items = list(answers.items())
        random.shuffle(items)
        answers = dict(items)

        #  grid the answers:
        #      A    B
        #      C    D
        Button(answer_frame, text=list(answers)[0], width=30, height=7, command=lambda: self.click_answer(answers[list(answers)[0]], question_text, answers)).grid(row=0, column=0)
        Button(answer_frame, text=list(answers)[1], width=30, height=7, command=lambda: self.click_answer(answers[list(answers)[1]], question_text, answers)).grid(row=0, column=1)
        Button(answer_frame, text=list(answers)[2], width=30, height=7, command=lambda: self.click_answer(answers[list(answers)[2]], question_text, answers)).grid(row=1, column=0)
        Button(answer_frame, text=list(answers)[3], width=30, height=7, command=lambda: self.click_answer(answers[list(answers)[3]], question_text, answers)).grid(row=1, column=1)


    #  execute command accoding to the answer
    def click_answer(self, run, question_text, answers):

        #  if correct
        if run == True:

            #  if not last question
            if self.right.count < 11:
                question_text.destroy()  # clear message from screen
                self.questions.remove(self.question)  # make sure same question not asked again
                self.right.count += 1
                self.right.count_label.config(text = f'PRIZE:\n{PRIZES[list(PRIZES)[self.right.count - 1]]}$')  # udate prize text
                self.ask_questions()  # go again

            #  user answered all questions correctly
            else:
                #  clear the screen
                question_text.destroy()
                self.middle.question_frame.grid_forget()
                self.middle.answer_frame.grid_forget()

                #  disable buttons
                self.right.skip.config(state = DISABLED)
                self.right.out.config(state = DISABLED)
                self.right.count += 1
                self.right.count_label.config(text = f'PRIZE:\n{PRIZES[list(PRIZES)[self.right.count - 1]]}$')

                end_label = Label(self.middle.frame, text='Congratulations, you have won 1 000 000$!\nWant to play again?', bg='#FFF', font=('Helvetica', 16), anchor='center')
                end_label.grid(row=0, padx=80, pady=20)

                restart_button = Button(self.middle.frame, text='RESTART', command=lambda: self.restart(end_label, restart_button))
                restart_button.grid(row=1, pady=20)

        #  if incorrect
        else:

            #  assign correct answer to variable
            for a in answers:
                if answers[a] == True:
                    correct_answer = a
                    break

                else:
                    pass

            #  clear the screen
            question_text.destroy()
            # self.middle.question_frame.grid_forget()
            self.middle.answer_frame.grid_forget()

            #  disable buttons
            self.right.skip.config(state = DISABLED)
            self.right.out.config(state = DISABLED)

            if 3 <= self.right.count <= 6:  # player won guaranteed 1 000$
                end_msg = f'Wrong answer!\nThe correct answer is {correct_answer}.\nYou won 1 000$, better luck next time !'

            elif 6 <= self.right.count <= 11:  # player won guaranteed 50 000$
                end_msg = f'Wrong answer!\nThe correct answer is {correct_answer}.\nYou won 50 000$, not bad !'

            else:  # player won nothing
                end_msg = f'Wrong answer!\nThe correct answer is {correct_answer}.\nYou won nothing, try again !'

            #  grid ending message
            end_label = Label(self.middle.frame, text=end_msg, bg='#FFF', font=('Helvetica', 16),  anchor='center')
            end_label.grid(row=0, pady=50)

            #  grid restart button
            restart_button = Button(self.middle.frame, text='RESTART', command=lambda: self.restart(end_label, restart_button))
            restart_button.grid(row=1, pady=30)


    #  skip current question and move to next one
    def skip_question(self):

        #  disable the skip button
        self.right.skip.config(state = DISABLED)

        #  clear frames
        for widget in self.middle.question_frame.winfo_children():
            widget.grid_forget()

        for widget in self.middle.answer_frame.winfo_children():
            widget.grid_forget()

        #  remove question from list
        self.questions.remove(self.question)

        #  continue
        self.ask_questions()


    #  disable CASH OUT and SKIP button
    #  clear the screen
    #  show ending message and restart button
    def cash_out(self):

        #  disable buttons
        self.right.skip.config(state = DISABLED)
        self.right.out.config(state = DISABLED)

        #  clear widgets
        for question in self.middle.question_frame.winfo_children():
            question.grid_forget()

        for answer in self.middle.answer_frame.winfo_children():
            answer.grid_forget()

        #  clear frames
        self.middle.question_frame.grid_forget()
        self.middle.answer_frame.grid_forget()

        #  end text
        end_label = Label(self.middle.frame, text=f'Congratulations, you have won {PRIZES[list(PRIZES)[self.right.count - 1]]}$ !\nWant to play again?', bg='#FFF', font=('Helvetica', 16))
        end_label.grid(row=0, padx=80, pady=50)

        #  restart
        restart_button = Button(self.middle.frame, text='RESTART', command=lambda: self.restart(end_label, restart_button))
        restart_button.grid(row=1, pady=30)


    #  clear screen
    #  update class attributes
    #  restart question loop
    def restart(self, label, button):

        #  clear
        label.destroy()
        button.destroy()

        #  update
        self.questions = list(QA)
        self.right.count = 0
        self.right.count_label.config(text = f'PRIZE:\n0$')

        #  restart
        self.start_with_skip()


def main():

    ui = UserInterface()
    ui.start()

if __name__ == '__main__':
    main()
