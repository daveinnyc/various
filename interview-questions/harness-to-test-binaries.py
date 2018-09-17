''' Explore funtionality of some unknown binary files. 
    
    Binary files are known to have some errors, construct a minimal test to find 
       the errors in each file

    Verify expected functionality 
    -- entry for each word in the input file
    -- line number for each word
    -- line numbers ascend
    -- one entry per line for a given word

'''

import os
import re
import hashlib
import subprocess


def get_binary_list():
    executables = []

    for filename in os.listdir('.'):
        if re.search(r'.bin$', filename):
           executables.append(filename)

    return executables


def get_unique_filename(data):
    return hashlib.md5(data.encode('utf-8')).hexdigest()


def get_output(binary_file, input_file):
    cmd_line = "./" + binary_file + " < " + input_file
    process_output = str(subprocess.check_output(cmd_line, shell=True), 'utf-8')
   
    output_lines = process_output.split('\n')
    # Last item is emptyline from output
    if output_lines[-1] == '':
        output_lines.pop()

    return(output_lines)


def create_input_file(test_input_data):   
    test_file =  get_unique_filename(test_input_data)

    try:
        test_input_file = open(test_file, 'w')

    except IOError as e:
        print('ERROR: {} - {}'.format(e.filename, e.strerror))
 
    else:   
        try:
            test_input_file.write(test_input_data)
        except IOError as e:
            print('ERROR: {} - {}'.format(e.filename, e.strerror))

    test_input_file.close()
    return(test_file)


def clean_up(filename):
    try:
        os.remove(filename)
    except OSError as e:
        print('ERROR: {} - {}'.format(e.filename, e.strerror))


def test_read_all_lines(binary_to_test):
    # Setup
    test_input = '''aaa
                    bbb
                    ccc
                 '''

    input_for_test = create_input_file(test_input)   
    program_output = get_output(binary_to_test, input_for_test)

    # Test
    expected_length = len(test_input.split('\n')) - 1
    if len(program_output) != expected_length:
       return "Fail {}, {} != {},  output: {}, input: {}".format(
                                                         "read_all_lines",
                                                         len(program_output),
                                                         expected_length,
                                                         program_output,
                                                         input_for_test)
        
    # Don't cleanup failed tests
    clean_up(input_for_test)
    
    return "PASS read all lines"

    

def test_no_final_line_return(binary_to_test):
    # Setup
    test_input = '''aaa
                    ccc '''

    input_for_test = create_input_file(test_input)   
    program_output = get_output(binary_to_test, input_for_test)

    # Test
    expected_length = len(test_input.split('\n'))
    if len(program_output) != expected_length:
       return "Fail {},  {} != {},  output: {}, input: {}".format(
                                                         "no final line return",
                                                         len(program_output),
                                                         expected_length,
                                                         program_output,
                                                         input_for_test)
        
    # Don't cleanup failed tests
    clean_up(input_for_test)
    
    return "PASS no final line return"



def test_multiple_words(binary_to_test):
    # Setup
    test_input = '''aaa
                    bbb bbb
                    ccc
                    ddd bbb
                    aaa bbb fff eee 
                 '''

    input_for_test = create_input_file(test_input)   
    program_output = get_output(binary_to_test, input_for_test)

    # Test
    expected_lengths = {"aaa":2, "bbb":3, "ccc":1, "ddd":1, "eee":1, "fff":1}

    output_dict = {}
    for entry in program_output:
        word_lines = entry.split()
        output_dict[word_lines[0]] = len(word_lines) -1

    failed_list = []
    for key, value in output_dict.items():
        if value != expected_lengths[key]:
            failed_list.append((key, value, expected_lengths[key]))

    if len(failed_list) > 0:
       return "Fail {} output: {}, input: {}".format("multiple words", 
                                                         failed_list,
                                                         input_for_test)
        
    # Don't cleanup failed tests
    clean_up(input_for_test)
    
    return "PASS multiple words"


def test_alphabetical_order(binary_to_test):
    # Setup
    test_input = '''bbb
                    abc
                    aaa
                    abb
                    ddd
                 '''

    input_for_test = create_input_file(test_input)   
    program_output = get_output(binary_to_test, input_for_test)

    # Test
    expected_order = ["aaa", "abb", "abc", "bbb", "ddd"]

    output_order = []
    for entry in program_output:
        word_lines = entry.split()
        output_order.append(word_lines[0])

    if output_order != expected_order:
       return "Fail {} output: {}, input: {}".format("alpabetical order", 
                                                         output_order,
                                                         input_for_test)
        
    # Don't cleanup failed tests
    clean_up(input_for_test)
    
    return "PASS alphabetical order"


########################
###   RUN IF MAIN    ###                       
########################
if __name__ == "__main__":
    binaries = get_binary_list()
    #binaries = ['main1.bin']
    for b in binaries:
        print("\nTESTING {}".format(b))
        print(test_read_all_lines(b))
        print(test_no_final_line_return(b))
        print(test_multiple_words(b))
        print(test_alphabetical_order(b))
        
# EOF
