# Generate some stats for an example of the birthday paradox problem
#
# Model a simulation of the bday problem
# https://en.wikipedia.org/wiki/Birthday_problem
#
# The scenario is based on showing random images from a directory containing
#    764 different image files and noting when repeats occur
#
# (c) 2019 Dave Cuthbert


# Solve for 50%
# 'How many images need to be displayed for a 50% chance of repetition?'

# P(A) is the probability of a collision
# P(A') is the probability of no collision
# P(A) = 1 - P(A')

from collections import defaultdict
import random

# num_files = 365      # Classic bday example for testing, 23 people @ 50.7%
num_files = 764       # Number of files in the actual sample



def test_samples():
    test_samples = defaultdict(lambda: 0)

    for n in range(1, num_files + 2):  # max + 1 (for python) + 1 = collision
        val = random.randint(1, num_files)  # randint include last value
        test_samples[val] += 1
        if test_samples[val] == 2:
            return n


def find_50_percent(num_items):
    memo = defaultdict(lambda:1)
    target_probability = .50

    memo[1] = 1       # remember the last value in the chain
    for i in range(1, num_items + 1):  # first val cached, python ends at (last-1)
        memo[i] = memo[i - 1] * ((num_items + 1 - i ) / num_items)

        if 1 - memo[i] > target_probability:
            print(f"Num for 50%: {i}, percentage: {100 * (1 - memo[i]):.2f}")
            return i


runs = find_50_percent(num_files)
print(f"For {num_files} it takes {runs}")

# According to the accepted bday paradox equation 764 files should see a
#  repetition after 33 files, 50% of the time
#
# Let's test that

samples = 0
num_test_runs = 5000
num_sample_groups = 100

for j in range(num_sample_groups):
    runs = 0
    for i in range(num_test_runs):
        runs += test_samples()
    # print(f"After {num_test_runs} runs the average is: "
    #      f"{(runs / num_test_runs):.2f}")       
    samples += runs

print(f"After {num_sample_groups} groups and "
      f"{num_sample_groups * num_test_runs} runs "
      f"the average is: {(samples / (num_test_runs * num_sample_groups)):.2f}")

