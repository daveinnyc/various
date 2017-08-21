'''
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
   the 6th prime is 13.

What is the 10 001st prime number?

Solution:
Copyright 2017 Dave Cuthbert 
License MIT
'''

def create_list_of_primes(): 
    list_of_primes = set([2])                   # Seed first prime to start
  
    is_prime = True
    prime_count = 1                             # First prime was seeded
    start = 2
    end = 10000

    while True: 
        for number in range(start, end):  # Start after last seeded prime
            for prime in list_of_primes:
                if number % prime == 0:
                    is_prime = False
                    break
            if is_prime == True:
                list_of_primes.add(number)
                prime_count += 1
            if prime_count == 10001:
                return sorted(list(list_of_primes))
            is_prime = True
        start = end + 1
        end = end + end


def solve_problem():
    prime_10001 = create_list_of_primes()

    return (prime_10001[-1])
           

if __name__ == "__main__":
        print(solve_problem())
