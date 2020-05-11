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
# Count backwards from 100 to 0 by 10s 
#   NOTE: stop value is not included
counts = list(range(100, -10, -10))
print(counts)


