import random

def choice():
    Person_choice=input("Enter your choice (stone,paper or scissor):")
    Option=["Stone" , "Paper" , "Scissor"]
    Computer_choice = random.choice(Option)
    Choices={"Person_choice":Person_choice,"Computer_choice":Computer_choice}
    return Choices

def who_win(Computer,Person):
    if Computer==Person:
        return "It's a tie"
    
    elif Computer=="Stone":
        if Person=="Paper":
            return "You win!"
        else:
            return "You loose!"
        
    elif Computer=="Paper":
        if Person=="Stone":
            return "You loose!"
        else:
            return "You win!"
        
    elif Computer=="Scissor":
        if Person=="Stone":
            return "You win!"
        else:
            return "You loose!"

move=choice()
print(move)
win=who_win(move["Computer_choice"],move["Person_choice"])
print(win)