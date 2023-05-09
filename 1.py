import random
l1 = ["stone","paper","scissor"]
rounds = int(input("how many rounds do u need:"))
comp_points = 0
user_points = 0
print('["stone","paper","scissor"]')
class game:
    def checker():
        global comp_points , l1 , user_points
        user_input = input("Enter ur choice:")
        comp_input = random.choice(l1)
        if user_input == comp_input:
            True
        elif user_input == "stone" and comp_input == "paper":
            comp_points = comp_points + 1
        elif user_input == "stone" and comp_input == "scissor":
            user_points = user_points + 1
        elif user_input == "paper" and comp_input == "stone":
            user_points = user_points + 1
        elif user_input == "paper" and comp_input == "scissor":
            comp_points = comp_points + 1
        elif user_input == "scissors" and comp_input == "paper":
            user_points = user_points + 1
        elif user_input == "scissors" and comp_input == "stone":
            comp_points = comp_points + 1
        else:
            print("Invalid Input")
            game.checker()

for i in range(rounds):
    game.checker()
        
print("Computer Points:",comp_points)
print("Player Points:",user_points)
if comp_points == user_points:
    print("DRAW, try again")
elif comp_points > user_points:
    print("Computer WINS !!!")
elif comp_points < user_points:
    print("Player WINS !!!")
else:
    print("Internal error")