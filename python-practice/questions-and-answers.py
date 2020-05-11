##########################################
###### Compare use of 'is' and '==' ######
##########################################
'''
# Create two lists
a = [1, 2, 3]
c = [1, 2, 3]
# Assign one list to a variable
b = a


# Verify eqivalence of contents
print("## Verify eqivalence of contents.")
print(f"a == b: {a == b}")
print(f"a == c: {a == c}")
print("")

# Display identity of objects
print("## Display identity of objects.")
print(f"a is b: {a is b}")
print(f"a is c: {a is c}")
print("")
print(f"ID a: {id(a)}")
print(f"ID b: {id(b)}")
print(f"ID c: {id(c)}")
print("")

# Add to the list, show variable updated too
a.append(4)
print("## Add to the list, show variable updated too.")
print(f"a: {a}")
print(f"b: {b}")
print("")

# Add to the variable, show list updated too
b.append(5)
print("## Add to the variable, show list updated too.")
print(f"a: {a}")
print(f"b: {b}")
print("")

# Make a copy of list a, verify differnt objects
d = a[:]
print("## Make a copy of list a, verify differnt objects.")
print(f"ID a: {id(a)}")
print(f"ID d: {id(d)}")
print("")

# Update the copied list, show original unchanged. 
d.append(6)
print("## Update the copied list, show original unchanged.")
print(f"a: {a}")
print(f"d: {d}")
print("")
'''

########################
###### Decorators ######
########################
'''
# A function that takes another function as an argument, 
#   does something, then executes the passed function

# Sample decorator
def decorator_function(input_function):
    def do_something():
        # Do something 
        print("Inside the decorator")
        print(f"Called: {input_fuction}")
        
        # Execute the original function
        input_function()
        
    return do_something()

# Sample functions
def func_one():
    print("ONE")
    
def func_two(input_string):
    print(input_string)
    
# Use the decorator
#@decorator_function
func_one()

#@decorator_function    
func_two("TWO")    
'''

############################
###### Range Operator ######
############################
'''
# Count backwards from 100 to 0 by 10s 
#   NOTE: stop value is not included
counts = list(range(100, -10, -10))
print(counts)
'''


###############################
###### Class defintition ######
###############################
# Define a class, instantiate it, return an instance value and a class value

class Sample:
    class_var = 100
    
    def __init__(self, a, b=10):
        self.a = a
        self.b = b
        
    def get_b(self):
        return self.b
        
sample_1 = Sample(1)
sample_2 = Sample(2, 20)

print(f"sample_1.a {sample_1.a}")
print(f"sample_2.a {sample_2.a}")
print("")
print(f"sample_1.b {sample_1.b}")
print(f"sample_1.b {sample_2.b}")
print("")
print(f"sample_1.class_var {sample_1.class_var}")
print(f"sample_1.class_var {sample_2.class_var}")

# Update class variable
Sample.class_var = 200
print("\n## Update class variable")
print(f"sample_1.class_var {sample_1.class_var}")
print(f"sample_1.class_var {sample_2.class_var}")
