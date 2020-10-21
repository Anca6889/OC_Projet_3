
class Leveltest:

    def __init__(self):

        
        self.structures = self.grid_gen()
        self.wall = wall

    def grid_gen(self):

        with open("level.txt", "r") as file:
            grid = file.readlines()
            for i in range(len(grid)):
                grid[i] = grid[i].strip()
        return grid

    def structures(self):
        y_pos = 0
        for lines in self.structure:
            x_pos = 0
            for letter in self.structures:
                if letter == "#":
                    self.structures.append(self.wall)
               
            
maps = Leveltest()
maps.grid_gen()
maps.structures()

print(maps.grid_gen())
print(maps.structures())
