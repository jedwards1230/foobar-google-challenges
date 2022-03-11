def solution(n):
    print()
    # base list to track data
    res = [1]+[0] * n
    
    # loop each combination of n
    for row in range(1, n + 1):
        print('row', row)
        print('a', res)
        
        # loop backwards from end of row -> middle
        # computing inner loop down in reverse to row 
        # allows list to be built from 0 -> n
        for col in range(n, row - 1, -1):
            print('col', col, '-', row)
            res[col] += res[col - row]
            
        print('b', res)
        print()
    
    print('c', res) 
    # single stair height doesnt work. sub 1
    res[n] -= 1
    print('d', res)
    
    print('\nres', res[n])
    
    return res[n]

assert(solution(3)) == 1
assert(solution(4)) == 1
assert(solution(5)) == 2
assert(solution(200)) == 487067745