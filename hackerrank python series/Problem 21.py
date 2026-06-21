# You are given a string  and width .
# Your task is to wrap the string into a paragraph of width .

# Function Description

# Complete the wrap function in the editor below.

# wrap has the following parameters:

# string string: a long string
# int max_width: the width to wrap to

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
# OR better way to code without using import

# def wrap(string,max_width):
#     for i in range(0,len(string),max_width):
#         print(string[i:i+max_width])
        
# wrap("asldkfjoasdifoasdjflasdkfoasdfoasdifop",2)