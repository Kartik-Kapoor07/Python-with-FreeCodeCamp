# Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc. for more details view problem directly

if __name__ == '__main__':
    s = input()
    
    # Initialize flags
    has_alnum = False
    has_alpha = False
    has_digit = False
    has_lower = False
    has_upper = False
    
    # Check every character in a single loop
    for char in s:
        if char.isalnum():
            has_alnum = True
        if char.isalpha():
            has_alpha = True
        if char.isdigit():
            has_digit = True
        if char.islower():
            has_lower = True
        if char.isupper():
            has_upper = True
            
    # Print results
    print(has_alnum)
    print(has_alpha)
    print(has_digit)
    print(has_lower)
    print(has_upper)