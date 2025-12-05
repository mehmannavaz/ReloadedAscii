import os

def getSize():
    """
    get `width` and `lenth` of terminal emulator.
    
    return: [177, 45]
    """
    width, lenth = os.get_terminal_size() # os.terminal_size(columns=177, lines=45)
    return [width, lenth]
