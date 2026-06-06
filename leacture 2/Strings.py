# Strings:Ordered, Immutable, text representation

# Double (") can be used where we have to use apostrophe(') in a string 
my_string= "I'm a programmer"
print(my_string)

# here we have to use the (') for string because inside the string we have to use the (")
Nelson_Mandela='Nelsom Mandela thoughts “I learned that courage was not the absence of fear, but the victory over it.”'

# for multiple lines use triple comma(""" or ''')

print("""You
are
beautiful,
Intelligent,
brave,
outstanding
just
believe
in
yourself.
""")

char=my_string[:7]
print(char)

greeting="Hello"
name="Kartik"
sentence= greeting+" "+name
print(sentence)

for i in sentence:
    print(i)
    
extra_space="   nExon   "
print(extra_space)

print(extra_space.strip())
print(extra_space.upper())
print(extra_space.lower())
print(extra_space.title())
print(extra_space.startswith('n'))# it check weather that is true or not
print(extra_space.count('o'))# it will count the number of same alphabets
print(extra_space.replace("   nExon   ","Nexon"))

my_list=Nelson_Mandela.split()# It splits all the words and convert that into a list
print(my_list)
print(my_list[1])

new_string='how ,you ,are ,doing ,in ,life.'
new_list=new_string.split(",")# this break down the words and convert that into a list and ignore comma due to this (",")
print(new_list)
new_string=''.join(new_list)
print(new_string)

# forget all bad code before now lets move on to more bad code

x=['a']*5

word=''

# insuffient method and more time consumer method 
for i in x:
    word +=x
    
Word = ''
Word= ''.join(my_list)

# Types of string in python: 
# %S make string varaible print in a double comma string
# %d make int varaible print in a double comma 
# f string make every type of varaible print latest

Drop_Bomb="Hiroshima"
Year=1945

print("Drop On %s"%Drop_Bomb)
print("Bomb was droped in year %d"%Year)
print("The USA drop an atomic bomb at %s in year %d" %( Drop_Bomb,Year))
print(f"On {Year} USA drop an atomic bomb at {Drop_Bomb}")