# Some notes on reading an article on static analysis: 
#    https://deepsource.io/blog/introduction-static-code-analysis/
'''
# Hello world example
import io
import tokenize


str1 = b"This is string one"
str2 = b"This is string two"

str1_upper = str1.upper()
str2_upper = str2.upper()

for input_str in [str1, str2, str1_upper, str2_upper]:
    for token in tokenize.tokenize(io.BytesIO(input_str).readline):
        print(token)
'''

# Sample foo finder
import sys
import tokenize

class FooChecker:
    # Finds instances of foo used as a function
    # - ignores comments, strings which use 'foo'
    msg = "foo found"

    def __init__(self):
        self.violations = list()
        
    def find_violations(self, filename, tokens):
        for token_type, token, (line, col), loc_end, src_line, in tokens:
            if token_type == tokenize.NAME:
                if token == "foo":                   
                    self.violations.append((filename, line, col, src_line))
                
    def check(self, files):
        for filename in files:
            with tokenize.open(filename) as fd:
                tokens = tokenize.generate_tokens(fd.readline)
                self.find_violations(filename, tokens)
                
    def report(self):
        for violation in self.violations:
            filename, line, col, src_line = violation
            print(f"{filename}:{line},{col}: {self.msg} :: {src_line}")
            
if __name__ == "__main__":
    files = sys.argv[1:]
    checker = FooChecker()
    checker.check(files)
    checker.report()
    
    
    
                
'''
###############
#### NOTES ####            
###############
# Command line invocation for debugging:
$> python3 -m tokenize -e <input_file>

# Original blog checker looked for a character: '
# This modified function only finds strings, not function or variable names
#   doesn't find strings properly either, needs to use 'in' instead of '=='
    def find_violations(self, filename, tokens):
        print("FINDING")
        for token_type, token, (line, col), _, _, in tokens:
            if token_type == tokenize.STRING:
                if token == "foo":                   
                    self.violations.append((filename, line, col))


'''
# EOF            