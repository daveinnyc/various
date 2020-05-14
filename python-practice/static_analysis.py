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
    msg = "foo found"

    def __init__(self):
        self.violations = list()
        
    def find_violations(self, filename, tokens):
        print("FINDING")
        for token_type, token, (line, col), _, _, in tokens:
            if (token_type == tokenize.STRING and (token == "foo")):
                self.violations.append((filename, line, col))
                
    def check(self, files):
        print("CHECKING")
        for filename in files:
            with tokenize.open(filename) as fd:
                tokens = tokenize.generate_tokens(fd.readline)
                self.find_violations(filename, tokens)
                
    def report(self):
        print("REPORTING")
        print(self.violations)
        for violation in self.violations:
            filename, line, col = violation
            print(f"{filename}: {line}, {col}: {self.msg}")
            
if __name__ == "__main__":
    files = sys.argv[1:]
    checker = FooChecker()
    checker.check(files)
    checker.report()
    
    
    
                
            
            