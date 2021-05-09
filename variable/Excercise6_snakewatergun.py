#snake water gun
import random
inc = 1
lost = 0
won = 0
while(inc<10):
    print("Choose any one from Snake(1), Water(2), Gun(3)")
    your_choice = int(input())
    list = ["Snake", "Water", "Gun"]
    Random_Choice = random.choice(list)
    print("Computer choice",Random_Choice)
    if your_choice == 1 and Random_Choice == "Snake":
        print("Tie dude")
    elif your_choice == 2 and Random_Choice == "Snake":
        lost = lost + 1
        print("You Lost",lost)
    elif your_choice == 3 and Random_Choice == "Snake":
        won = won + 1
        print("You Won",won)
    elif your_choice == 1 and Random_Choice == "Water":
        lost = lost + 1
        print("You Lost",lost)
    elif your_choice == 2 and Random_Choice == "Water":
        print("Tie dude")
    elif your_choice == 3 and Random_Choice == "Water":
        won = won + 1
        print("You Won",won)
    elif your_choice == 1 and Random_Choice == "Gun":
        won = won + 1
        print("You Won",won)
    elif your_choice == 2 and Random_Choice == "Gun":
        lost = lost + 1
        print("You Lost",lost)
    elif your_choice == 3 and Random_Choice == "Gun":
        print("Tie dude")
    inc = inc+1
    print("Chance number ", inc)
if lost>won:
    print("You lost the game, Better luck next time")
elif lost<won:
    print("Congratulations, You won")
elif lost==won:
    print("Tie Dude")