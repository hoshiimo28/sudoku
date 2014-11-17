#sudoku
import sys
from sudoku.SudokuStage import Sudoku
from sudoku.SudokuResolver import *

def main():
    sd = Sudoku(sys.argv[1])
    print "-----------------------------------------"
    print "INPUT:"
    sd.out()            
    print "-----------------------------------------"
    print "TRIAL 1:"
    resolver = LogicalResolver(sd)
    resolver.sudoku.out()            
    if not resolver.sudoku.verify():
        print "-----------------------------------------"
        print "TRIAL 2:"
        resolver = BacktrackingResolver(resolver.sudoku)
        resolver.sudoku.out()

if __name__=='__main__':
    main()
