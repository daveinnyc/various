'''

Imagine the output of a parser that consists of statements [.], errors [x], 
  calls [(] and returns [)]. The output should be a shortened path that 
  drops any statements, calls and returns that complete without error. 

  e.g.  (...(.x)(..))  ==> (...(.x))  Drops: (..)
        (.((...(..()..).x)...))  ==> (.((.x)...))  Drops: ...(..()..)

Task:  Given an input string return the correct condensed output

Copyright 2017, Dave Cuthbert. License MIT
'''
class Statements():
    def __init__(self):
        self.statements = '' 

    def get_statement(self):
        return self.statements

    def set_statement(self, statement_string):
        self.statements = statement_string

    def add_statements(self, statement_string):
        self.statements += statement_string


def match_parens(statements):
    output_list = []
    error_flag = False
    recursive_step = (error_flag, [], 0)
    index = 0
   
     
    while index < len(statements):
        element = statements[index]
        if element == '(':
            recursive_step = match_parens(statements[index + 1:])
            index += recursive_step[2] + 1 
            output_list.append('(')
            output_list.extend(recursive_step[1])
            output_list.append(')')
            if recursive_step[0] == True:
                error_flag = True       # Don't just toggle, may already be True
        if element == '.':
            output_list.append('.')
        if element == 'x':
            output_list.append('x')
            error_flag = True
        if element == ')':
            if error_flag == False:
                output_list = []
            return (error_flag, output_list, index)
        index += 1

    return (error_flag, ''.join(output_list))
            

def match_parens_test():
    '''
    # Almost empty list
    >>> start = Statements()
    >>> start.set_statement('()')
    >>> match_parens(start.get_statement())
    (False, '()')

    # List with statements and one error
    >>> start = Statements()
    >>> start.set_statement('(..x.)')
    >>> match_parens(start.get_statement())
    (True, '(..x.)')

    # List with just one call/return level
    >>> start = Statements()
    >>> start.set_statement('(..(..).)')
    >>> match_parens(start.get_statement())
    (False, '()')

    # List with statements and two errors
    >>> start = Statements()
    >>> start.set_statement('(x..x.)')
    >>> match_parens(start.get_statement())
    (True, '(x..x.)')

    # List with multiple  call/return level
    >>> start = Statements()
    >>> start.set_statement('(..(..)(..).)')
    >>> match_parens(start.get_statement())
    (False, '()')

    # List with nested call/return 
    >>> start = Statements()
    >>> start.set_statement('(...(.(..).).)')
    >>> match_parens(start.get_statement())
    (False, '()')

    # List with trailing error 
    >>> start = Statements()
    >>> start.set_statement('(...(.(..).)x.)')
    >>> match_parens(start.get_statement())
    (True, '(...()x.)')

    # List with nested error 
    >>> start = Statements()
    >>> start.set_statement('(...(.(.x.).).)')
    >>> match_parens(start.get_statement())
    (True, '(...(.(.x.).).)')

    # List with nesting and nested error 
    >>> start = Statements()
    >>> start.set_statement('(...(.(.(..(...)).)(.x.).).)')
    >>> match_parens(start.get_statement())
    (True, '(...(.()(.x.).).)')
    '''


if __name__ == "__main__":
    import doctest
    doctest.testmod()
