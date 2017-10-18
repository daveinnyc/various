'''
Problem  026

A unit fraction contains 1 in the numerator. The decimal representation of the 
  unit fractions with denominators 2 to 10 are given:

1/2 =   0.5
1/3 =   0.(3)
1/4 =   0.25
1/5 =   0.2
1/6 =   0.1(6)
1/7 =   0.(142857)
1/8 =   0.125
1/9 =   0.(1)
1/10    =   0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be 
  seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle 
  in its decimal fraction part.


Technique: move through the remainders using mod and bumping by 10x each time. 

Solution: Copyright 2017 Dave Cuthbert, MIT License
'''

def solve_problem():
    longest_denominator = [1, 1]
        
    for denominator in range(10, 1001):
        remainder = 1 % denominator
        divisor = int(1 / denominator)
        cycle = ''
        cycle_set = set()
        no_repetitions = True

        while no_repetitions:
            remainder *= 10
            divisor = int(remainder / denominator)  
            remainder = remainder % denominator
            if remainder in cycle_set:
                no_repetitions = False
                position = cycle.find(str(remainder))
            else: 
                cycle += str(divisor)
                cycle_set.add(remainder)
        
        if (len(cycle) - position) > longest_denominator[1]:
            longest_denominator[0] = denominator
            longest_denominator[1] = len(cycle) - position
        print("{}: {}".format(denominator, cycle))

 
    return(longest_denominator[0])



if __name__ == "__main__":
    print(solve_problem())
