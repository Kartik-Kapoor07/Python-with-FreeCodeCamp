"""You need to perform N commands on the list. The possible commands are:

1. insert i e
   - Insert integer e at position i.

2. print
   - Print the current list.

3. remove e
   - Remove the first occurrence of integer e.

4. append e
   - Add integer e to the end of the list.

5. sort
   - Sort the list in ascending order.

6. pop
   - Remove the last element from the list.

7. reverse
   - Reverse the order of the list.

Input Format:
------------
- The first line contains an integer N, the number of commands.
- The next N lines each contain one command.

Output Format:
-------------
- For every "print" command, print the current state of the list.

Example:

Input:
------
4
append 1
append 2
insert 1 3
print

Operations:
-----------
append 1   -> [1]
append 2   -> [1, 2]
insert 1 3 -> [1, 3, 2]
print      -> [1, 3, 2]

Output:
-------
[1, 3, 2]

Goal:
-----
Read each command, perform the corresponding list operation,
and print the list whenever the command is "print".
"""

if __name__ == '__main__':
    N = int(input())
    mylist = list()
    
    for i in range (N):
        parts = input().split()
        command = parts[0]
        
        if command == "insert":
            index = int(parts[1])
            value = int(parts[2])
            mylist.insert(index,value)
        
        elif command == "print":
            print(mylist)
        
        elif command == "remove":
            value = int(parts[1])
            mylist.remove(value)
            
        elif command == "append":
            value = int(parts[1])
            mylist.append(value)
            
        elif command == "sort":
            mylist.sort()

        elif command == "remove":
            value = int(parts[1])
            mylist.remove(value)
            
        elif command == "pop":
            mylist.pop()
        
        elif command == "reverse":
            mylist.sort(reverse=True)       