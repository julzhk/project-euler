def Ulam2(n, k):
    """
    An integer sequence defined as follows:
 
        U(n, 1) = n
        U(n, 2) = 2n + 1
        U(n, k: k > 2) = min{U(n, k - i) + U(n, k - j): i, j < k; i != j; sum is unique}
 
        e.g. first 16 terms of U(2, k) sequence:
 
            2, 5, 7, 9, 11, 12, 13, 15, 19, 23, 27, 29, 35, 37, 41, 43, ...
    """
    if k == 1:
        return n
    elif k == 2:
        return 2*n + 1
    terms = [n, 2*n + 1]
    min_bound = terms[1]

    sums = {}

    i = 3

    while(i < k):
        combs = combinations(terms, 2)
        print('terms={}, combs={}, sums={}'.format(terms, list(combs), sums))
        for c in combs:
            s = sum(c)
            t = tuple(c)
            print('s={}, t={}'.format(s, t))
            if s not in sums:
                sums[s].append(t) if isinstance(sums[s], list) else sums.update({s: [t]})
            elif s in sums and t not in sums[s]:
                sums[s].append(t)
        print('sums={}'.format(sums))
        #terms.append(min(s for s in sums if len(sums[s]) == 1 and s > min_bound))
        #min_bound = terms[-1]
        break
       
    return terms[-1]

