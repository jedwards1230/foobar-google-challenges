import math
from itertools import product

def solution(src, dest):
    if src == dest:
        return 0
    # Point to row, col
    def to_coords(pt):
        return int(math.floor(pt / 8)), int(pt % 8)
    
    def to_point(x, y):
        return x + y * 8
    
    def possible_moves(pt):
        x, y = pt
        # get all possible moves (horizontal + vertical moves) with cartesian product
        moves = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
        # filter out illegal moves
        moves = [(x,y) for x,y in moves if x >= 0 and y >= 0 and x < 8 and y < 8]
        return moves
    
    x, y = int(math.floor(src / 8)), int(src % 8)
    
    moves = possible_moves((x, y))
    moves = [to_point(x, y) for x, y in moves]
    res = 0
    arr = []
    
    while True:
        res += 1
        # cycle all moves
        for move in moves:
            # look for final destination
            if move == dest:
                return res
            # prepare list for next stage of moves
            arr.extend(possible_moves(to_coords(move)))
            # remove duplicates to reduce higher level recursion cycle count
            arr = list(set(arr))
        moves = [to_point(x, y) for x, y in arr]
        arr = []

x = solution(0, 0)
print(x)