import timeit

def add(num, reps):
    return_value = 0
    for i in range(reps):
        return_value += num
    
    return return_value

    
def multiply(num, reps):
    return num * reps
        

if __name__ == "__main__":
    NUM = 5
    REPS = 10

    print(f"ADD: {NUM} {REPS}")
    # Can't pass a function directly. Timeit needs a callable thing so use lambda
    # number defaults to 3 repetitions, left at default to show syntax
    print(min(timeit.repeat(lambda: add(NUM, REPS), number=50)))
    print()
    print(f"MULTIPLY: {NUM} {REPS}")
    print(min(timeit.repeat(lambda: multiply(NUM, REPS), number=50)))
