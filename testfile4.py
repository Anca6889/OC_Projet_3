for line in self.level:
    y += 1
    coord[y, x] = line
    for letter in line:
        x += 1
        coord[x, y] = letter
