import time
import os
import keyboard
import pynput.keyboard


class Menu:
    def __init__(self):
        self._index = 0
        self.history = History()
        self._menu = ["Count  ", "History", "Exit   "]
        self.select()
        while True:
            if keyboard.is_pressed('up'):
                self.index('up')
            elif keyboard.is_pressed('down'):
                self.index('down')
            elif keyboard.is_pressed('space'):
                if self._index == 2:
                    break
                elif self._index == 0:
                    calculate = Calc(self.history)
                    self.select()
                elif self._index == 1:
                    self.history.read()
                    pause()
                    self.select()
            time.sleep(0.1)

    def select(self):
        clear()
        string = str()
        for lines in range(len(self._menu)):
            if lines != self._index:
                string += self._menu[lines] + "\n"
            else:
                string += self._menu[lines] + " * \n"
        print(string)

    def index(self, up_down):
        if up_down == "up":
            if self._index == 0:
                self._index = len(self._menu) - 1
            else:
                self._index -= 1
        elif up_down == "down":
            if self._index == len(self._menu) - 1:
                self._index = 0
            else:
                self._index += 1
        self.select()


class Calc:

    def __init__(self, history):
        time.sleep(0.1)
        clear()
        self.history = history  # type: History
        self._index = 0
        self._menu = ["+", "-", "*", "/", "//", "%", "**"]
        num1 = get_num()
        self.select()
        while True:
            if keyboard.is_pressed('left'):
                self.index('up', num1)
            elif keyboard.is_pressed('right'):
                self.index('down', num1)
            elif keyboard.is_pressed('space'):
                break
            time.sleep(0.1)
        num2 = get_num()
        print(self.calculate(num1, num2, self._index))
        pause()

    def select(self):
        for lines in range(len(self._menu)):
            if lines != self._index:
                print(self._menu[lines] + " | ", end="")
            else:
                print(self._menu[lines] + " . | ", end="")
        print()

    def index(self, up_down, num):
        clear()
        print(num)
        if up_down == "up":
            if self._index == 0:
                self._index = len(self._menu) - 1
            else:
                self._index -= 1
        elif up_down == "down":
            if self._index == len(self._menu) - 1:
                self._index = 0
            else:
                self._index += 1
        self.select()

    def calculate(self, n1, n2, i):
        if i == 0:
            result = n1 + n2
            self.history.write(str(n1) + " + " + str(n2) + " = " + str(result))
            return str(n1) + " + " + str(n2) + " = " + str(result)
        elif i == 1:
            result = n1 - n2
            self.history.write(str(n1) + " - " + str(n2) + " = " + str(result))
            return str(n1) + " - " + str(n2) + " = " + str(result)
        elif i == 2:
            result = n1 * n2
            self.history.write(str(n1) + " * " + str(n2) + " = " + str(result))
            return str(n1) + " * " + str(n2) + " = " + str(result)
        elif i == 3:
            if n2 == 0:
                self.history.write(str(n1) + " / " + str(n2) + " = !!! division by zero !!!")
                return "!!! division by zero !!!"
            else:
                result = n1 / n2
                self.history.write(str(n1) + " / " + str(n2) + " = " + str(result))
                return str(n1) + " / " + str(n2) + " = " + str(result)
        elif i == 4:
            if n2 == 0:
                self.history.write(str(n1) + " // " + str(n2) + " = !!! division by zero !!!")
                return "!!! division by zero !!!"
            else:
                result = n1 // n2
                self.history.write(str(n1) + " // " + str(n2) + " = " + str(result))
                return str(n1) + " // " + str(n2) + " = " + str(result)
        elif i == 5:
            if n2 == 0:
                self.history.write(str(n1) + " % " + str(n2) + " = !!! division by zero !!!")
                return "!!! division by zero !!!"
            else:
                result = n1 / n2
                self.history.write(str(n1) + " % " + str(n2) + " = " + str(result))
                return str(n1) + " % " + str(n2) + " = " + str(result)
        elif i == 6:
            result = n1 ** n2
            self.history.write(str(n1) + " ^ " + str(n2) + " = " + str(result))
            return str(n1) + " ^ " + str(n2) + " = " + str(result)


class History:

    def __init__(self):
        self.filename = './history.txt'
        if not os.path.exists(self.filename):
            self.file = open(self.filename, 'a')
            self.file.close()

    def read(self):
        clear()
        with open(self.filename) as file:
            for lines in file:
                print(lines)
        file.close()

    def write(self, line):
        with open(self.filename, "r+") as file:
            file.seek(0, 2)
            file.writelines(line + "\n")
            file.close()


def get_num():
    x = True
    while True:
        pause()
        print("Enter the digit: ")
        num = input()
        try:
            float(num)
            break
        except ValueError:
            x = True

    return float(num)


def clear():

    os.system('cls')


def pause():
    try:
        print("Press space to continue...")
        keyboard.wait('space')
    except SyntaxError:
        pass

calc = Menu()
keyboard.
# his = History()
# calc1 = Calc(his)


