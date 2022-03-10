from fractions import Fraction


def solution(m):
    # [Q, R]
    # [0, I]
    def get_sub_matrices(m, n_transients):
        Q, R, Z, I = [], [], [], []

        for r in range(n_transients):
            qRow = []
            for c in range(n_transients):
                qRow.append(m[r][c])
            Q.append(qRow)

        for r in range(n_transients):
            rRow = []
            for c in range(n_transients, len(m[r])):
                rRow.append(m[r][c])
            R.append(rRow)
        
        for i in range(len(Q), len(m)):
            Z.append(m[i][:len(Q[0])])
        
        # creates I based on size of Q
        m = []
        for i in range(len(Q)):
            r = []
            for j in range(len(Q)):
                r.append(int(i == j))
            I.append(r)
            
        return Q, R, Z, I
    
    # returns matrix in standard form
    def to_standard_form(m):
        # swap rows to maintain matrix
        def swap(m, i, j):
            n = []
            s = len(m)

            # dont need to swap if they're equal
            if i == j:
                return m

            for r in range(s):
                nRow = []
                tmpRow = m[r]
                if r == i:
                    tmpRow = m[j]
                if r == j:
                    tmpRow = m[i]
                for c in range(s):
                    tmpEl = tmpRow[c]
                    if c == i:
                        tmpEl = tmpRow[j]
                    if c == j:
                        tmpEl = tmpRow[i]
                    nRow.append(tmpEl)
                n.append(nRow)
            return n
        
        zero_row = -1
        for i in range(len(m)):
            sum = 0
            for j in range(len(m)):
                sum += m[i][j]
            if sum == 0:
                # we have found all-zero row, remember it
                zero_row = i
            if sum != 0 and zero_row > -1:
                # we have found non-zero row after all-zero row - swap these rows
                n = swap(m, i, zero_row)
                # and repeat from the begining
                return to_standard_form(n)
            
        # place a 1 on each terminal state
        for i in range(len(m)):
            if m[i][i] <= 1:
                m[i][i] = 1
        return m
    
    
    def multiply_matrix(m1, m2):
        m = []

        # length of first matrix
        for r in range(len(m1)):
            row = []
            # length of second matrix
            for c in range(len(m2[0])):
                sum = 0
                for i in range(len(m1[0])):
                    sum += m1[r][i] * m2[i][c]
                row.append(sum)
            m.append(row)
        return m
    

    # functions to inverse amtrix (m^1)
    def get_fundamental_matrix(I, Q):
        # subtract two matrices
        def subtract_matrix(i, q):
            s = []
            for r in range(len(i)):
                sRow = []
                for c in range(len(i[r])):
                    sRow.append(i[r][c] - q[r][c])
                s.append(sRow)
            return s
        
        def transpose_matrix(m):
            return map(list,zip(*m))

        def get_matrix_minor(m,i,j):
            return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

        def get_matrix_determinant(m):
            # case for 2x2 matrix
            if len(m) == 2:
                return m[0][0]*m[1][1]-m[0][1]*m[1][0]

            determinant = 0
            for c in range(len(m)):
                determinant += ((-1)**c)*m[0][c]*get_matrix_determinant(get_matrix_minor(m,0,c))
            return determinant
        
        m = subtract_matrix(I, Q)
        determinant = get_matrix_determinant(m)
        # case for 2x2 matrix:
        if len(m) == 2:
            return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                    [-1*m[1][0]/determinant, m[0][0]/determinant]]

        #find matrix of cofactors
        cofactors = []
        for r in range(len(m)):
            cofactorRow = []
            for c in range(len(m)):
                minor = get_matrix_minor(m,r,c)
                cofactorRow.append(((-1)**(r+c)) * get_matrix_determinant(minor))
            cofactors.append(cofactorRow)
        cofactors = transpose_matrix(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c]/determinant
        return cofactors
    
    
    def sanitize(m):
        def gcd(a ,b):
            if b==0:
                return a
            else:
                return gcd(b,a%b)
        
        needed = m[0]
        # float to simple fractions
        to_fraction = [Fraction(i).limit_denominator() for i in needed]
        
        # find lowest common denominator
        lcm = 1
        for i in to_fraction:
            if i.denominator != 1:
                lcm = i.denominator
        for i in to_fraction:
            if i.denominator != 1:
                lcm = lcm*i.denominator/gcd(lcm, i.denominator)
        
        lcm = int(lcm)
        to_fraction = [(i*lcm).numerator for i in to_fraction]
        to_fraction.append(lcm)
        return to_fraction

    
    if len(m)==1:
        if len(m[0]) == 1 and m[0][0] == 0:
            #print([1, 1])
            return [1, 1]
            
    # sort matrix
    m = to_standard_form(m)
    
    sums = [sum(i) for i in m]
    n_transients = 0
    
    # convert each int to a probability
    for i in range(len(m)):
        if sums[i] > 1:
            n_transients += 1
        n = 0.
        for j in range(len(m[0])):
            if sums[i] >= 1:
                n += m[i][j]
        if n != 0:
            for j in range(len(m[0])):
                if sums[i] >= 1:
                    m[i][j] = m[i][j] / n
    
    # find sub matrices
    Q, R, Z, I = get_sub_matrices(m, n_transients)
        
    # Do matrix math
    F = get_fundamental_matrix(I, Q)
    FR = multiply_matrix(F, R)

    return sanitize(FR)


assert(solution([[0, 2, 1, 0, 0], 
                [0, 0, 0, 3, 4], 
                [0, 0, 0, 0, 0], 
                [0, 0, 0, 0,0], 
                [0, 0, 0, 0, 0]])) == [7, 6, 8, 21]


assert(solution([[0, 1, 0, 0, 0, 1], 
               [4, 0, 0, 3, 2, 0], 
               [0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0], 
               [0, 0, 0, 0, 0, 0]])) == [0, 3, 2, 9, 14]