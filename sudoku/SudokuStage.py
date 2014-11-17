import csv

class Sudoku:
    def __init__(self, file):
        self.stage = []
        with open(file, 'rb') as f:
            reader = csv.reader(f, delimiter=',');
            for i, row in enumerate(reader):
                self.stage.append([])
                for j, item in enumerate(row):
                    self.stage[i].append(int(item) if len(item) > 0 else 0)
    
    def getat(self, x, y):
        return self.stage[y][x]
    
    def setat(self, x, y, num):
        self.stage[y][x] = num

    def check(self, num, x, y):
        v = self.vsearch(num, x)
        h = self.hsearch(num, y)
        b = self.bsearch(num, x, y)
        return (v == h == b == None)

    def vsearch(self, num, x):
        for y in range(9):
            if num == self.stage[y][x]:
                return y
        return None
    
    def hsearch(self, num, y):
        for x in range(9):
            if num == self.stage[y][x]:
                return x
        return None

    def bsearch(self, num, x, y):
        for i in range(3):
            for j in range(3):
                sx = (x / 3) * 3 + j
                sy = (y / 3) * 3 + i
                if num == self.stage[sy][sx]:
                    return sx, sy
        return None
    
    def candidates(self, x, y):
        res = []
        for num in range(1, 10):
            if self.check(num, x, y):
                res.append(num)
        return res

    def out(self):
        for y in range(9):
            for x in range(9):
                n = self.stage[y][x]
                print n if n != 0 else "-", " ",
            print ""

    def verify(self):
        for i in range(9):
            if len(set(self.stage[i])) != 9:
                return False
            if len(set([self.stage[j][i] for j in range(9)])) != 9:
                return False
        for i in range(9):
            items = []
            bx = (i % 3) * 3
            by = (i / 3) * 3
            for j in range(9):
                x = bx + (j % 3)
                y = by + (j / 3)
                items.append(self.getat(x, y))
                if self.getat(x,y) == 0:
                    return False
            if len(set(items)) != 9:
                return False
        return True
    
                


        
