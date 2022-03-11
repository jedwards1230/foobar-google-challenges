def solution(num_buns, num_required):
    return 1


assert(solution(2, 1)) == [[0], [0]]
assert(solution(4, 4)) == [[0], [1], [2], [3]]
assert(solution(5, 3)) == [[0, 1, 2, 3, 4, 5], 
                           [0, 1, 2, 6, 7, 8], 
                           [0, 3, 4, 6, 7, 9], 
                           [1, 3, 5, 6, 8, 9], 
                           [2, 4, 5, 7, 8, 9]]