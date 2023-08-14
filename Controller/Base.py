import os
import time
from Keys.input import KeyboardInput

class Base:

    def __init__(self):
        self._optionsList = list()
        self._optionListLength = 0
        self.userInput = KeyboardInput()

    def get_optionListLength(self):
       return self._optionListLength
    
    def get_options(self):
        return [item[0] for item in self._optionsList]
    
    def clearOptions(self):
        self._optionsList.clear()

    def printOptions(self):
        for index, item in enumerate(self._optionsList):
            print(f'{index + 1}. {item[0]}')
    
    def runFunc(self, id: int):
        self._optionsList[id - 1][1]()

    def runLoop(self):
        self._optionListLength = len(self._optionsList)
        while not self.userInput.compare(str(self._optionListLength +1)):

            print("Enter one of the options: \n")
            self.printOptions()
            print(f"{len(self._optionsList)+1}. Quit")
            self.userInput.set_value("\n> ")

            if self.userInput.get_value() == str(self._optionListLength + 1):
                os.system("cls")
                break
            
            elif self.userInput.get_value().isnumeric() and 0 < int(self.userInput.get_value()) <= self._optionListLength:
                os.system("cls")
                self.runFunc(int(self.userInput.get_value()))

            else:
                os.system("cls")
                
                self.userInput.disable()

                print(f"\nOption \"{self.userInput.get_value()}\" does not exist, please try again.")
                time.sleep(3)

                self.userInput.enable()

                os.system("cls")