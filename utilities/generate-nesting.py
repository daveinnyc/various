# Generate a deeply nested json document for upload to a mongodb instance
#
# $> python3 generate-nesting.py 200 > nest.json                                                                                                           
# $> mongoimport --host 127.0.0.1 --port 27440 --db test \
#                --collection nested --authenticationDatabase admin \
#                --username USR --password PWD --file nest.json
#


import sys

if len(sys.argv) != 2:
   print("USAGE: python3 generate-nesting.py NEST_LEVEL")
   sys.exit()


NEST_DEPTH = int(sys.argv[1])

jsonstring_elements = []
jsonstring = ''

for n in range(NEST_DEPTH):
  jsonstring_elements.append( f'{{ "nest{n}": ' )

jsonstring = ' '.join(jsonstring_elements)
jsonstring += f'"True" {NEST_DEPTH * "}"}'

print(jsonstring)
