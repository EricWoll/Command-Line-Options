from Controller.Base import Base

class Auto(Base):

    def __init__(self):
        super().__init__()
    
    def addOption(self, option: str, funcLink) -> None:
        self.optionsList.append( [option, funcLink] )
    
    def removeOption(self, option: str) -> None:
        for index, item in enumerate(self.optionsList):
            if item[0] == option:
                del self.optionsList[index]
        self.optionListLength -= 1