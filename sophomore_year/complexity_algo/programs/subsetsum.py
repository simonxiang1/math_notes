def subsetsum(X, T, i=0):
    """Find a subset of X that sums to T.

    Inputs:
        X: a list of positive integers, e.g. [1, 4, 5]
        T: a target positive integer, e.g. 9
        i: index we're looking at [so X[i:] is of interest]

    Outputs:
        None or a list that sums to T (e.g., [4, 5])
    """

    #base cases
    if T == 0:
        return []
    if len(X) <= i or T < 0:
        return None

    #recursion
    take = subsetsum(X[1:], T - X[0])
    if take is not None:
        return [X[0]] + take
    skip = subsetsum(X[1:], T)
    return skip

print(subsetsum([1, 4, 5], 9))

import random
vals = [random.randint(10000, 20000) for _ in range(5)]
T = sum(v * random.randint(0, 1) for v in vals)
print(f"Instance: {vals} {T}")

print((subsetsum(vals, T)))
