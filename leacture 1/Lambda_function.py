# singler liner function are called as lambda function
Number=[]
for i in range (1,201):
    Number.append(i)

even_nums = list(filter(lambda x: x % 2 == 0, Number)) 
print(even_nums)