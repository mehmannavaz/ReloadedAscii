Example1 = """
 _
|_|
"""

Example2 = """    
 __________  
|  __  __  |
| |  ||  | |
| |__||__| |
|          | 
|__________|
"""

Example3 = """
         __
       _|  |_
     _|      |_
    |  _    _  |
    | |_|  |_| |
 _  |  _    _  |  _
|_|_|_| |__| |_|_|_|
  |_|_        _|_|
    |_|      |_|
"""

class ascii:
    def __init__(self, art):
        self.art = art
        self.length = art.count('\n')
        self.width = max([len(line) for line in art.split('\n')])

        # Turned
        # https://github.com/mehmannavaz/ReloadedAscii/blob/main/docs/01-Theory/02-HowToTurn
        self.turned_art = ""
        self.turned_length = self.length + 1 
        self.turned_width = self.width + 5


def calculateTurnedWidth:


def _in_box:
    """
    check if it's inside a box or not
    """
    pass

for line in Example1:
    