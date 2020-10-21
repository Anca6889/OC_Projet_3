

class Level1:
    """Class setting up the level 15x15,
    Draw of the level is on level.txt file with following parameters:
    
    # = Wall
    - = Path
    0 = Start (and Mcgayver initial position)
    1 = End
    G = Guardian position """

    def __init__(self):

        self.game_grid = self.game_grid()
        self.wall = self.wall()
        self.path = self.path()
        self.start = self.start()
        self.end = self.end()
        self.guardian_position = self.guardian_position()
        self.macgayver_position = self.macgayver_position()

    def game_grid(linesnumber, columnumber):
        game_grid = [[]] * linesnumber
        for line in range(linesnumber):
            game_grid[line] = [0] * columnumber
        return game_grid
    
    game_grid(15,15)
    print(game_grid)

    level = open("level.txt", "r")
    
    level.close()


level = Level1()

-------------------------------------------------------
class Labyrinth:
    """
    Create labyrinth in a dictionary and display it.
    """

    def __init__(self):

        self.position = {}
        with open("level.txt", "r") as file:
            row = 0
            for y in file:
                column = 0
                for x in y:
                    self.position[(column, row)] = x
                    column += 1
                row += 1
        

maps = Labyrinth


    




