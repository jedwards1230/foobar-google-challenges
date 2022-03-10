def solution(M, F):
    # Divide the smaller one into the bigger one, 
    # round down to find out the multiplier to 
    # increase the counter and to subtract the larger one to find the answer faster.
    
    # a = 2
    # b = 4
    
    # a - (b * count) = a % b
    # b * count = a - a % b
    # count = (a - (a % b)) / b
    
    # 2 - (4 * count) = (2 % 4) = 2
    # c = x
    def shortcut(a, b):
        count = 1
        if a == 1:
            count = b - 1
            b = 1
        elif b == 1:
            count = a - 1
            a = 1
        elif a > 1 or b > 1:
            count = int((a - (a % b)) / b)
            a = a - (b * count)
        
        return a, b, count
    
    def check_end(a, b):
        end = False
        s = False
        
        # check for winners
        if a == 1 and b == 1:
            end = True
            s = True
        if a == 0 and b == 1 or a == 1 and b == 0:
            end = True
            s = True
            
        # check for edge cases
        if a == b:
            end = True
        if a < 1 or b < 1:
            end = True
            
        return end, s
                
    mi = int(M)
    fi = int(F)
    end = False
    success = False
    count = 0
    
    while not end and not success:
        c = 1
        
        if fi > mi:
            fi, mi, c = shortcut(fi, mi)
        elif mi > fi:
            mi, fi, c = shortcut(mi, fi)
        
        end, success = check_end(mi, fi)
            
        count += c
            
    if success:
        res = str(count)
    else:
        res = 'impossible'
    
    return res

print
x = solution('100', '99')
x = solution(str(10**50), '1')
x = solution('0', '0')

assert(solution('2', '4')) == 'impossible'
assert(solution('4', '7')) == '4'
assert(solution('2', '1')) == '1'