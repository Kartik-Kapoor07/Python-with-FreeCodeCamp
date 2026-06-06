from collections import Counter,defaultdict,deque,namedtuple

# Counter count the number of words or letter in string or list and return the output from desecding order
Word1 = "Apple"
print(Counter(Word1))

# it has the ability to customize the append,remove,route etc can be modified highly
number= deque([1,2,3])

number.appendleft(9)
number.append(12)
print(number)
number.pop()
number.popleft()
print(number)
number.rotate(2)# shifts every thing two step forward and for list indexed things shift them into zero index

# namedtuple
students= namedtuple("student",["name","age"])
s=students("kartik",15)
print(s)

# Default value
# this create a group of same key more effient to store
students = defaultdict(list)

data = [("A","Kartik"), ("A","Rahul"), ("B","Aman")]

for cls, name in data:
    students[cls].append(name)
    
print(students)


