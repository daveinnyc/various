# Some code to use with pdb
# Use with: python3 -m pdb debugger.py

def adder(number):
    plus_one = number + 1
    return plus_one

def loops(number):
    var_sum = 0
    for i in range(number):
        var_sum += adder(i)
    return var_sum

if __name__ == "__main__":
    print(f"Result: {loops(4)}")
