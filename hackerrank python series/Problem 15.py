# Task
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

def split_and_join(line):
    break_line = line.split(" ")
    Join_line = "-".join(break_line)
    return Join_line
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)