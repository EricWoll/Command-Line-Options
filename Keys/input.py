import keyboard

class KeyboardInput:

    def __init__(self):
        self._value = ""
        
    def enable(self):
        for i in range(150):
            keyboard.unblock_key(i)

    def disable(self):
        for i in range(150):
            keyboard.block_key(i)

    def set_value(self, prompt):
        self._value = input(prompt)

    def get_value(self):
        return self._value 
    
    def compare(self, comparison):
        return self._value == comparison