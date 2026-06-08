# in file handling there is a thing pointer cursor but in pointer once it go forward it can apply all the operation where the pointer so to make pointer go back we can use     f.seek(0)  (move pointer to beginning)



# the w mode help to create a new file and if file already exists it replace all the text with new text
print("--Creating a new txt file--")
with open("leacture 2\File handling\Sample.txt","w") as f:
    f.write("I'm kartik.\nI am currently learning python")


# the r mode stands for the read only mode its work is to read the data and print that mainly
print("--Reading a existing file--")
with open("leacture 2\File handling\Sample.txt","r") as f:
    print(f.read())


# the a mode help to write the things on the end of the file
print("--Adding content at the end of a file")
with open("leacture 2\File handling\Sample.txt","a") as f:
    f.write("\nWant to get admission in thapar university.")
    f.write("\n1,2,3,4,5,6,7,8,9,10,11")


# line by line reading content and then printing
print("--Reading line by line")
with open("leacture 2\File handling\Sample.txt","r") as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    line4 = f.readline()
    
    print(line1)
    print(line2)
    print(line3)
    print(line4)


# finding the even and odd number from the file
print("--Finding odd and even numbers--")
with open(r"leacture 2\File handling\Sample.txt","r") as f:

    data = f.readlines()
    # Last line contains numbers
    numbers = data[-1].split(",")

    for num in numbers:
        num = int(num)

        if num % 2 == 0:
            print(num, "is Even")
        else:
            print(num, "is Odd")

# in this folder i also add a image for a quick revision of all the modes in this