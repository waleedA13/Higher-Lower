from art import logo, vs
from game_data import data
from random import choice





#Checks if you got the answer
def answer(follower1, follower2, compare):
    if follower2 > follower1:
        return compare == 'b'
    elif follower1 > follower2:
        return compare == 'a'


#Gives a random celebrity
def celebrity():
    person = choice(data)
    return person


#Prints the first person and second person and then returns theirs follower count
def followers(person1, person2):
    if person1 == person2:
        person2 = celebrity()
    print(f"\nCompare A: {person1['name']}, a {person1['description']}, from {person1['country']}.")

    print(vs)

    print(f"Against B: {person2['name']}, a {person2['description']}, from {person2['country']}.")
    return person1['follower_count'], person2['follower_count']




in_game = True
while in_game:
    score = 0
    print(logo)
    person1 = celebrity()
    person2 = celebrity()

    comparing = True
    while comparing:
        follower1, follower2 = followers(person1, person2)
        checking = True


        while checking:
            compare = input("Who has more followers? A or B? ").lower()
            if compare != "a" and compare != "b":
                print("Invalid! Try again!")
            else:
                checking = False

        if answer(follower1, follower2, compare):
            score += 1
            print(f"You're right. Current score is: {score}.\n")
            person1 = person2
            person2 = celebrity()
        else:
            print(f"You lost! Your final score is: {score}.\n")
            comparing = False
        

    end_game = True

    #Asks if you want to end the game or keep playing
    while end_game:
        end = input("Type yes to keep playing, else type no. ").lower()
        if end != 'no' and end != 'yes':
            print("Invalid! Try Again!")
        else:
            end_game = False
            if end == 'no':
                in_game = False