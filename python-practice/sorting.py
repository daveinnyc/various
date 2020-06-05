# Use lambda for sorting

l = [{'a': 10, 'b': 'a'}, 
     {'a': 9, 'b': 'b'}, 
     {'a': 8, 'b': 'c'}, 
     {'a': 7, 'b': 'd'}
    ]

# Sorts the list, no assingment needed
l.sort(key=lambda item: item['a'])

print(l)