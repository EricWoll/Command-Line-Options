def typeInput(inputPrompt: str, inputType: type, incorrectMsg: str):
    '''
    Loops until user input matches desired variable type.

    Args:
    - inputPrompt (str): Prints to screen to tell user what to input
    - inputType (type): The desired variable type that the user input will match
    - incorrectMsg (str): Prints message to screen when incorrect variable type is given

    Returns:
    - changedInput (???): The users response given as desired type
    '''
    correctInputType = False
    while not correctInputType:
        userInput = input(inputPrompt)

        try:
            changedInput = inputType(userInput)
            correctInputType = True
        except:
            print(incorrectMsg)

    return changedInput