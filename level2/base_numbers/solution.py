def solution(n, b):
    def toBaseN(n, b):
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
        for i in range(len(digits)):
            digits[i] = str(digits[i])
        return int(''.join(digits[::-1]))
    
    def toDecimal(n, b):
        res = 0
        for d in str(n):
            res = b * res + int(d)
        return res
    
    k = len(n)
    z = n
    res = []
    
    while z not in res:
        # add to stored IDs
        res.append(z)
        
        # sort and init variables
        s = sorted(z)
        x = ''.join(s[::-1])
        y = ''.join(s)
        
        # compute z depending upon base
        if b == 10:
            z = int(x) - int(y)
            z = str(z)
        else:
            z = int(toDecimal(x, b)) - int(toDecimal(y, b))
            z = toBaseN(z, b)

        # take care of leading 0
        z = str(z)
        z =  (k - len(z)) * '0' + z
    return len(res) - res.index(z)


res = solution('210022', 3)
print(res)