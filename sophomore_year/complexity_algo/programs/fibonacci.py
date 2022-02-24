def f(n):
    if n <= 1: return n
    return f(n-1) + f(n-2)

memo = {}
def f2(n):
    if n in memo: return memo[n]
    if n <= 1: return n
    ans = f2(n-1) + f2(n-2)
    memo[n] = ans
    return ans

def fibdp(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs[n]

def fibwindow(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

print(f(30))
print(f2(30))
print(fibdp(100))
