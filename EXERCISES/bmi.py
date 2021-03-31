"""
COMP.CS.100 Body Mass Index
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""

from tkinter import *


class Userinterface:


    def __init__(self):

        #  main window
        self.__mainwindow = Tk()

        #  attributes
        self.__weight_value = Entry(self.__mainwindow)
        self.__height_value = Entry(self.__mainwindow)
        self.__calculate_button = Button(self.__mainwindow, text='Calculate', background='green',foreground='white' , command=self.calculate_BMI)
        self.__result_text = Label(self.__mainwindow, text='')
        self.__explanation_text = Label(self.__mainwindow, text='')
        self.__stop_button = Button(self.__mainwindow, text='Stop', background='red', foreground='white', command=self.stop)

        #  grid
        self.__weight_value.grid(row=0, column=0)
        self.__height_value.grid(row=0, column=1)
        self.__calculate_button.grid(row=0, column=2)
        self.__stop_button.grid(row=1, column=0, columnspan=3)
        self.__result_text.grid(row=2, column=0)
        self.__explanation_text.grid(row=3, column=0)


    def calculate_BMI(self):

        # test for ValueError
        try:
            weight = float(self.__weight_value.get())
            height = float(self.__height_value.get()) * 0.01

        except ValueError:

            #  print error msg and clear fields
            self.__result_text['text'] = 'Error: height and weight must be numbers.'
            self.reset_fields()
            return

        # test that nums are positive
        if weight > 0:
            if height > 0:
                pass

            else:

                #  print error msg and clear fields
                self.__result_text['text'] = 'Error: height and weight must be positive.'
                self.reset_fields()
                return
        else:

            #  print error msg and clear fields
            self.__result_text['text'] = 'Error: height and weight must be positive.'
            self.reset_fields()
            return

        #  bmi  =  weight  /  height^2
        bmi = weight / height**2
        self.__result_text['text'] = f'{bmi:.2f}'

        # execute explanation text
        if bmi < 18.5:
            self.__explanation_text['text'] = 'You are underweight.'

        elif 18.5 <= bmi <= 25:
            self.__explanation_text['text'] = 'Your weight is normal.'

        else:
            self.__explanation_text['text'] = 'You are overweight.'


    def reset_fields(self):

        self.__weight_value.delete(0, 'end')
        self.__height_value.delete(0, 'end')


    def stop(self):

        self.__mainwindow.destroy()

    #  initialize event loop
    def start(self):

        self.__mainwindow.mainloop()


def main():

    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
