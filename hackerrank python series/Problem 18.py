# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

# Sample Input
# ABCDCDC
# CDC

# Sample Output
# 2

def count_substring(string, sub_string):
    counter = 0
    start = 0
    end = len(sub_string)
    
    while end <= len(string):
        if sub_string == string[start:end]:
            counter += 1 
        start += 1
        end +=1
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    
# solve by taking help of Amir Charkhi, PhD youtuber