from cmdOptions.Controller.Base import Base

class Auto(Base):

    def __init__(self):
        super().__init__()
    
    def addOption(self, option: str, funcLink) -> None:
        self._optionsList.append( [option, funcLink] )
        self._optionListLength = len(self._optionsList)
    
    def removeOption(self, option: str) -> None:
        for index, item in enumerate(self._optionsList):
            if item[0] == option:
                del self._optionsList[index]
        self._optionListLength -= 1