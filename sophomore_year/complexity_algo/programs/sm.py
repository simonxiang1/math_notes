#ben's program

def x(M, W):
    all_permutations_of_M = itertools.permutations(M)
    def is_stable(M, W):
        for i in range(0, len(M)):
            m = M[i]
            w = W[i]
            for m2 in M:
                if m != m2 and prefers(w, m2, m):
                    return False
   
