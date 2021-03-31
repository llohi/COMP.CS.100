"""
COMP.CS.100 Counter
Tekijä: Joose Lohi
Opiskelijanumero: 0500800360
"""

from tkinter import *

class Counter:

    def __init__(self):

            self.__root = Tk()
            self.__value = 0

            self.__current_value = Label(self.__root , text=self.__value)
            self.__current_value.grid(row=0, column=0, columnspan=4)

            self.__reset_button = Button(self.__root , text='Reset', command=lambda: self.on_click('r'))
            self.__reset_button.grid(row=1, column=0)

            self.__increase_button = Button(self.__root , text='Increase', command=lambda: self.on_click('+'))
            self.__increase_button.grid(row=1, column=1)

            self.__decrease_button = Button(self.__root , text='Decrease', command=lambda: self.on_click('-'))
            self.__decrease_button.grid(row=1, column=2)

            self.__quit_button = Button(self.__root , text='Quit', command=self.__root.quit)
            self.__quit_button.grid(row=1, column=3)

            self.__root.mainloop()



    def on_click(self, x):

        if x == 'r':
            self.__value = 0
            self.__current_value.config(text = self.__value)

        elif x == '+':
            self.__value += 1
            self.__current_value.config(text = self.__value)

        elif x == '-':
            self.__value -= 1
            self.__current_value.config(text = self.__value)


def main():

    Counter()


if __name__ == '__main__':
    main()
