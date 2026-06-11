import secrets

students = [
    "Kartik",
    "Rahul",
    "Aman",
    "Priya"
]

print(secrets.randbelow(10))# just like randrange but secure 

# take any 4 digit bit combination like [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]]
print(secrets.randbits(4))
print(secrets.choice(students))#  just like random.choice just secure version
print(secrets.token_hex(8))# just a random hexadecimal but random 
print(secrets.token_urlsafe(16))# creates a url
