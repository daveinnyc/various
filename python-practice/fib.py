def fib_iter(n):
    count = 0
    first = 0
    second = 1
    
    while count < n:
        if n == 0:
           return 0
        if n == 1:
            return 1      
        
        first, second = first + second, first
        count += 1
        
    return first


if "__main__" == __name__:
    # Test values
    print(f"0 {fib_iter(1)}")
    print(f"1 {fib_iter(1)}")
    print(f"3 {fib_iter(3)}")
    print(f"5 {fib_iter(5)}")
