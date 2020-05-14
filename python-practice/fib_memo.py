memo = {0:0, 1:1}

def fib(n):
    #if n == 0: return 0
    #if n == 1: return 1
    
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]


if __name__ == "__main__":
    print(f"\n0: {fib(0)}")
    print(f"\n1: {fib(1)}")
    print(f"\n5: {fib(5)}")
    print(f"\n10: {fib(10)}")

    #for k,v in memo.items(): print(f"{k}: {v}") 
