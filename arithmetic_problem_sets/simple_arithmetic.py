''' Generate simple addition and subtraction problems
    for math practice
    
    Author: Dave Cuthbert
    Copyright: 2016
    License: MIT
''' 
import random
MAX_NUM_RANGE = 10
MAX_BASE_NUMBER = 10

def num_range(max_num):
    random.seed()
    nums_start = range(0,max_num+1)
    nums = []
    while len(nums_start) > 0:
        i = random.randint(0, len(nums_start)-1)
        nums.append(nums_start[i])
        del nums_start[i]
           
    return nums

def addition(base_number):
    addends = num_range(MAX_NUM_RANGE)
    problems = []
    for a in addends:
        problems.append((base_number, a))
        
    return problems

def subtraction(base_number):
    subtrahends = num_range(MAX_NUM_RANGE)
    problems = []
    for s in subtrahends:
        if s > base_number:
            problems.append((s, base_number))
        else:
            problems.append((base_number, s))
        
    return problems


def print_problems(problem_type, problem_elements):
    if 'add' == problem_type:
        sign = '+'
    elif 'subtract' == problem_type:
        sign = '-'
        
    counter = 0
    output_string = '<TABLE>'
    print_top_line = []
    print_bottom_line = []
    
    for a in problem_elements:
        print_top_line.append(a[0])
        print_bottom_line.append(a[1])
        counter += 1
        if 5 == counter:
            #Make each row of problems a small table   
            output_string += '<TABLE>'             

            #Top row
            output_string += '<TR>'
            for v in print_top_line:
                output_string += '<TD align="right" width="5%">' + str(v) + '</TD>'
                output_string += '<TD width="15%"> </TD>'
            output_string += "</TR>"

            #Bottom Row
            output_string += '<TR>'
            for v in print_bottom_line:
                output_string += '<TD align="right">' + sign + str(v) + '</TD>'
                output_string += '<TD> </TD>'
            output_string += "</TR>"

            #Underbar
            output_string += '<TR>'
            for c in range(counter):
                output_string += '<TD align="right" valign="top">____</TD>'
                output_string += '<TD> </TD>'
            output_string += "</TR>"

            output_string += '</TABLE>'             
            
            #Put vertical space between the problem rows    
            output_string += "<BR>" * 4
            #Reset values for next line
            counter = 0
            print_top_line = []
            print_bottom_line = []
    
            
    return output_string


def print_html_open():
    return "<HTML>"

def print_header():
    header_open = "<HEAD>"
    title = "<TITLE></TITLE>"
    header_close = "</HEAD>"
    return header_open + title + header_close

def print_body_open():
    return "<BODY>"

def print_set_font():
    return "<FONT face='verdana' size='3'>"

def print_body_close():
    return "</BODY>"
        
def print_html_close():
    return "</HTML>"                

if '__main__' == __name__:
    
    for pt in ['add', 'subtract']:
        #Loop to create 10*counter math problem sets using each 
        #  integer from 1 to MAX_BASE_NUMBER as basis for a set
        for i in range(1, MAX_BASE_NUMBER + 1):
            problem_elements = []
            for counter in range(3):
                if 'add' == pt:
                    problem_elements += addition(i)
                elif 'subtract' == pt:
                    problem_elements += subtraction(i)
                else:
                    print "Bad problem type specifier"
                    
            #Print the output as an html file
            output_file_string = ''
            output_file_string += print_html_open()
            output_file_string += print_header()
            output_file_string += print_body_open()
            output_file_string += print_set_font()
            output_file_string += print_problems(pt, problem_elements)
            output_file_string += print_body_close()
            output_file_string += print_html_close()
            output_file_name =  pt + "." + str(i) + ".html"
            output_file = open(output_file_name, 'w')
            output_file.write(output_file_string)
            output_file.close()
                    
#EOF