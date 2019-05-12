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


def test_samples(n_files):
    test_samples = defaultdict(lambda: 0)

    for n in range(1, n_files + 2):  # max + 1 (for python) + 1 = collision
        val = random.randint(1, n_files)  # randint include last value
        test_samples[val] += 1
        if test_samples[val] == 2:
            return n


def test_n_samples(num_samples, n_files):
    test_samples = defaultdict(lambda: 0)

    for n in range(num_samples):
        val = random.randint(1, n_files)  # randint include last value
        test_samples[val] += 1

    collision_count = 0
    multi_crash = 0
    for k,v in test_samples.items():
        if v == 2:
            collision_count += 1
        elif v > 2:
            multi_crash += 1

    return (collision_count, multi_crash)


def find_50_percent(num_items):
    memo = defaultdict(lambda:1)
    target_probability = .50

    memo[1] = 1       # remember the last value in the chain
    for i in range(1, num_items + 1):  # first val cached, python ends at (last-1)
        memo[i] = memo[i - 1] * ((num_items + 1 - i ) / num_items)

        if 1 - memo[i] > target_probability:
            print(f"Num for 50%: {i}, percentage: {100 * (1 - memo[i]):.2f}")
            return i


##########
## Main ##
##########
# num_files = 365      # Classic bday example for testing, 23 people @ 50.7%
num_files = 764        # Number of files in the actual sample

# Find out how many files are needed to get to 50% likelihood of collision
runs = find_50_percent(num_files)
print(f"For {num_files} it takes {runs}")

# According to the bday paradox equation 764 files should see a
#  repetition after 33 files, 50% of the time
#
# Let's test that
samples = 0
repetitions = 5000
num_sample_groups = 100

for j in range(num_sample_groups):
    runs = 0
    for i in range(repetitions):
        runs += test_samples(num_files)
    samples += runs

print(f"After {num_sample_groups} groups and "
      f"{num_sample_groups * repetitions} runs "
      f"the average is: {(samples / (repetitions * num_sample_groups)):.2f}")


# Every 10 minutes there are about 70 files displayed.
#   let's see how many collisions are expected at random
num_samples = 70
repetitions = 1000
single_collisions = 0
multi_collisions = 0
for count in range(repetitions):
    crashes = test_n_samples(num_samples, num_files)
    single_collisions += crashes[0]
    multi_collisions += crashes[1]

print(f"After {repetitions} repetitions of {num_samples} files each, "
      f"there are {single_collisions / repetitions} single and "
      f"{multi_collisions / repetitions} multiple crashes per group")
