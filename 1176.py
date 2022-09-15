def fib(n, computed = {0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fib(n-1, computed) + fib(n-2, computed)
    return computed[n]

T = int(input())
for x in range(0,T):
    N = int(input())
    print("Fib(%d) = %d" %(N,fib(N)))