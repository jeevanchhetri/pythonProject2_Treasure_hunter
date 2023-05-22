print("Welcome to Treasure Island \nYour mission to find the treasure.")
play_again = "y"
while play_again == "y":

    user_answer = input("You are at the crossroad. Where do you want to go? Left or Right: \n>>>").lower()

    if user_answer == "left":
        user_answer = input(
            "You came to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a "
            "boat. Type 'swim' to swim across \n>>>").lower()
        if user_answer == "wait":
            user_answer = input("You arrived at the island unharmed. There is a house with three doors. One red, "
                                "one yellow and one blue which color do you choose? \n>>>").lower()
            if user_answer == "red":
                print("Burned by fire. Game over.")
                play_again = input("Play Again?? 'Y' r 'N'\n>>").lower()
            elif user_answer == "yellow":
                print("You win!!")
                play_again = "n"
            elif user_answer == "blue":
                print("Eaten  by beasts. Game Over")
                play_again = input("Play Again?? 'Y' r 'N'\n>>").lower()
            else:
                print("Game over")
                play_again = input("Play Again?? 'Y' r 'N'\n>>").lower()
        else:
            print("Attacked by trout. Game Over.")
            play_again = input("Play Again?? 'Y' r 'N'\n>>").lower()

    else:
        print("Fall into a hole. Game Over")
        play_again = input("Play Again?? 'Y' r 'N'\n>>").lower()
