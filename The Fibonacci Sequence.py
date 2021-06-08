"The Fibonacci Sequence"

def fib(n):
    pred, curr = 0, 1 
    k = 1
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr

fib(6)
8
fib(2)
1
fib(9)
34

def fib(n):
    pred, curr = 1, 0
    k = 0
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr

"The answers are the same as the last block of code, no real change occured"