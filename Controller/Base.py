import os
import time
from Keys.input import KeyboardInput

class Base:

    def __init__(self):
        self.optionsList = list()
        self.optionListLength = 0
        self.userInput = KeyboardInput()
    
    def clearOptions(self):
        self.optionsList.clear()

    def printOptions(self):
        for index, item in enumerate(self.optionsList):
            print(f'{index + 1}. {item[0]}')
    
    def runFunc(self, id: int):
        self.optionsList[id - 1][1]()

    def runLoop(self):
        self.optionListLength = len(self.optionsList)
        while not self.userInput.compare(str(self.optionListLength +1)):

            print("Enter one of the options: \n")
            self.printOptions()
            print(f"{len(self.optionsList)+1}. Quit")
            self.userInput.set_value("\n> ")

            if self.userInput.get_value() == str(self.optionListLength + 1):
                os.system("cls")
                break
            
            elif self.userInput.get_value().isnumeric() and 0 < int(self.userInput.get_value()) <= self.optionListLength:
                os.system("cls")
                self.runFunc(int(self.userInput.get_value()))

            else:
                os.system("cls")
                
                self.userInput.disable()

                print(f"\nOption \"{self.userInput.get_value()}\" does not exist, please try again.")
                time.sleep(3)

                self.userInput.enable()

                os.system("cls")