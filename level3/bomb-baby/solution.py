import math


def solution(M, F):
    # Divide the smaller one into the bigger one, 
    # round down to find out the multiplier to 
    # increase the counter and to subtract the larger one to find the answer faster.
    # a = 35
    # b = 10
    # x = 
    # a - (b * x) = y
    # a - y = b * x
    # (a - y) / b = x
    # 35 - (10 * x) = 5, a
    # c = x
    def shortcut(a, b):
        count = 0
        if a > 3 or b > 3:
            x = int((a - (a % b)) / b)
            #print(f'1 - a: {a} | b: {b} | x: {x}')
            a = a - (b * x)
        
        return a, b, count
    
    def activate_bombs(a, b):
        return a - b
    
    def check_end(mi, fi):
        end = False
        s = False
        if mi == 1 and fi == 1:
            end = True
            s = True
        if mi == 0 and fi == 1 or mi == 1 and fi == 0:
            end = True
            s = True
        # check for edge cases
        if mi == fi:
            end = True
        if mi < 1 or fi < 1:
            end = True
        return end, s
                
    mi = int(M)
    fi = int(F)
    end = False
    success = False
    
    mi, fi, count = shortcut(mi, fi)
    
    while not end:
        #print(mi, fi)
        
        # check for success
        end, success = check_end(mi, fi)
        
        if fi > mi:
            end, success = check_end(fi, mi)
            fi = activate_bombs(fi, mi)
        elif mi > fi:
            end, success = check_end(mi, fi)
            mi = activate_bombs(mi, fi)
        
        if success:
            break
        else:
            count += 1
    
    if success:
        res = str(count)
    else:
        res = 'impossible'
    
    return res

x = solution('100', '99')
x = solution(str(10**50), str(10**49))

assert(solution('2', '4')) == 'impossible'

assert(solution('4', '7')) == '4'

assert(solution('2', '1')) == '1'