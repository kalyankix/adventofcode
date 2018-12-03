#!/usr/bin/env python
input_file = 'inputs.txt'

# read input file
input_file_contents = open(input_file, "r")
overall_result=0
for i in input_file_contents:
    overall_result = overall_result + int(i)
print overall_result