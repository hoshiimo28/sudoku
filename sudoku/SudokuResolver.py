from SudokuStage import Sudoku
import copy
import sys
class LogicalResolver:
    def __init__(self, sudoku):
        flag = True
        self.sudoku = copy.deepcopy(sudoku)
        while flag:
            flag = False
            for y in range(9):
                for x in range(9):
                    if self.sudoku.getat(x, y) != 0:
                        continue
                    n =  self.sudoku.candidates(x, y)
                    if len(n) == 1:
                        self.sudoku.setat(x, y, n[0])
                        flag = True


class BacktrackingResolver:
    def __init__(self, sudoku):
        self.stack = []
        self.sudoku = sudoku
        self.count = 0
        self.search(0)
        sudoku = self.sudoku
    
    def search(self, xy):
        self.count += 1
        clen = (self.count / 500)% 20 
        msg = "\rSEARCHING%s%s" % (">" * clen, " " * (20 - clen))
        sys.stdout.write(msg)
        sys.stdout.flush()
        x = xy % 9
        y = xy / 9
        if xy >= 9 * 9:
            print "\r%s" % (" " * 50)
            return True     

        if self.sudoku.getat(x, y) != 0:
            return self.search(xy + 1)
        
        self.stack.append(copy.deepcopy(self.sudoku))
        candidates = self.sudoku.candidates(x, y)

        if len(candidates) == 0:
            self.sudoku = self.stack.pop()
            return False

        for num in candidates: 
            self.sudoku.setat(x, y, num)
            if self.search(xy + 1):
                return True

        self.sudoku = self.stack.pop()
        return False

