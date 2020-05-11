####################################
### Compare use of 'is' and '==' ###
####################################
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

##################################################