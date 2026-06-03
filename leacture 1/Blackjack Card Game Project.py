print("   ██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗  ")
print("   ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝  ")
print("   ██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝   ")
print("   ██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗   ")
print("   ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗  ")
print(" ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ")
#
#                 ♠ ♥ ♦ BLACKJACK 21 ♦ ♥ ♠
#              Beat the Dealer Without Busting!

"""
# This game have the following rules:


# The deck is 52 in size.

# The Jack/Queen/King all count as 10. 
# The Ace can count as 11 or 1 depending on the user.
# It also have the list of number from 2 to 10.
# With the cards there are also Heart, Diamond, Club and Spade to increase the number of cards in the deck.

# The dealer will give 2 cards to player and 2 cards to itself.
# One of the dealer cards will be hidden until the end.
# If the value of dealer card is below 17 according to the rules he have to pick up another card.
# The player can decide to pick up another card or pass. 

#If the player's score is higher than dealer's score the player win. Same for  dealer.
# If the player's score is above 21 he lose the game. Same for dealer.
# If both scores are equal the game is draw.

# In this you also bet money if win you get double of your bet. 
# If lose you lose the money you bet. 
# If draw you get your money back.

# In this game the card is suffeled and dealer can only give uppermost card to player and to himself.And then uppermost card is removed from the deck. 
"""

import random

# list of the category of cards and the card
Category = ["Heart", "Diamond", "Club", "Spade"]
Card = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

Player_cards=[]
Player_score = 0

Dealer_cards=[]
Dealer_score = 0

# make a another list deck to store the card and category together and then to suffle the cards
Deck = [card + " of " + category for card in Card for category in Category]
random.shuffle(Deck)

# Brust function
def Bust_function(score):
    if score > 21:
        return True
    else:
        return False

# Resubality if else statements
def card_value(splitted_card, current_score,player=False):

    if splitted_card[0] == "Ace":

        if player and current_score < 11:
            while True:
                choose = input("You got an Ace! Choose 1 or 11: ")

                if choose in ["1", "11"]:
                    return int(choose)

                print("Wrong input.")

        elif current_score < 11:
            return 11

        else:
            return 1

    elif splitted_card[0] in ["Jack", "Queen", "King"]:
        return 10

    elif splitted_card[0].isdigit():
        return int(splitted_card[0])

    else:
        print("Something went wrong.")
        return None
 
# function for player cards
def player_Cards_function():
    global Player_score
    global Player_cards

    for i in range(2):
        temporary_card = Deck.pop()
        splitted_temporary_card= temporary_card.split()

        plus=card_value(
            splitted_temporary_card,
            Player_score,
            True
        )

        Player_score +=plus
        Player_cards.append((temporary_card,plus))
        print(f"You got {temporary_card}")
        print(f"Current score: {Player_score}\n")

# function for the dealer
def Dealer_cards_function():
    global Dealer_score

    for i in range(2):
        temporary_card = Deck.pop()
        splitted_temporary_card= temporary_card.split()

        plus=card_value(
            splitted_temporary_card,
            Dealer_score,
            False
        )

        Dealer_score +=plus
        Dealer_cards.append((temporary_card,plus))
           
# Print the player and dealer cards
def Print_cards():
    global Player_cards
    global Dealer_cards
    print(f"Your cards are: {Player_cards}")
    print(f"First card of Dealer is: {Dealer_cards[0]}\n")

# Player more card function
def Hit_Stand():
    global Player_score
    while True:
        if Player_score ==21 or Player_score > 21:
            break
        else:        
            Choice= (input("Do you want another card [(H)it or (S)tand]:")).upper()
            if Choice == 'H' or Choice =='HIT':
                temporary_card = Deck.pop()
                splitted_temporary_card= temporary_card.split()

                plus=card_value(
                    splitted_temporary_card,
                    Player_score,
                    True
                )

                Player_cards.append((temporary_card,plus))
                Player_score +=plus
                print(f"You got {temporary_card}")
                print(f"Current score: {Player_score}")

            elif Choice == 'S' or Choice == 'STAND':
                print("You dont want another card.\n")
                break

            else:
                print("Something went wrong.")
                return

    if Bust_function(Player_score):
        print("Bust! Dealer won the game.")
        return
    else:
        is_required_more_number_for_dealer()

# Functoin for the checking and making dealer number 17 or above
def is_required_more_number_for_dealer():
    global Dealer_score
    while Dealer_score <17:

        temporary_card = Deck.pop()
        splitted_temporary_card= temporary_card.split()

        plus=card_value(
            splitted_temporary_card,
            Dealer_score,
            False
        )
    
        Dealer_score += plus
        Dealer_cards.append((temporary_card,plus))
    
    if Bust_function(Dealer_score):
        print("Bust! Player won the game.")
        return
    else:
        printing_all_cards_with_value()
        winner()

# Print all cards
def printing_all_cards_with_value():
    global Player_cards
    global Dealer_cards

    print("--Your cards are--")
    for i in Player_cards:
        print(i)
    
    print("\n\n--Dealer cards are--")
    for i in Dealer_cards:
        print(i)

# who wins function
def winner():
    global Player_score
    global Dealer_score

    if Player_score==Dealer_score:
        print("This is draw.")
    elif Player_score>Dealer_score:
        print("CONGRATULATION! You won.")
    else:
        print("Dealer won.")

player_Cards_function()
Dealer_cards_function()
Print_cards()
Hit_Stand()