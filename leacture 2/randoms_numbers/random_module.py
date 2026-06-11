import random

fruits = ["Apple", "Banana", "Mango"]
students = [
    "A",
    "B",
    "C",
    "D",
    "E"
]

print(random.random())#it print a range of numbers between the 0 and 1
print(random.uniform(1,10))# it prints a float value between 1 and 9.99
print(random.randint(1,10))# it print the random integer from 1 to 10 and also include upper limit number
print(random.randrange(1,10))# it is same like .choice but dont reqiure a list
print(random.randrange(1,10,2))# ,2 make a range of number like (1,3,5,7,9)
print(random.choice(fruits))# it take a list of number and make a random choice
print(random.sample(students,2))#it takes a list and make multiple choice in this case multiple choise will be 2 duplicate are not possible
print(random.choices(students, k=5))# it is just like .sample but dont allows the duplicate
print(random.shuffle(fruits))# it suffels the items in a list

random.seed(1)#start the random machice from position 1 random uses a formula and keep the output same usefull for testing things for same input image in a system when we enter 5 it shows error then we will want to test that using 5 again after fixing then due to seed that number remain the same
print(random.randint(1,10))

# never use for important thins like crypto and bankaccount it is predictable
# using the randcrack module 
