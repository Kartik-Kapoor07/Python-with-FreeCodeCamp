# Task
# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# For Example:

# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  

def swap_case(s):
    result = ""
    for i in range(len(s)):
        if s[i].islower():
            result += s[i].upper()
        elif s[i].isupper():
            result += s[i].lower()
        else:
            result += s[i]
    return result
        
            
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
    

# * Or the better way is to use 

# *def swap_case(s):
# *   return s.swapcase()