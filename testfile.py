class Labyrinth:
    """
    Create labyrinth in a dictionary and display it.
    """

    def __init__(self):

        self.position = {}

    def genmap(self):
        with open("level.txt", "r") as file:
            row = 0
            for y in file:
                column = 0
                for x in y:
                    self.position[(column, row)] = x
                    column += 1
                row += 1
        

maps = Labyrinth
maps.genmap()


    
