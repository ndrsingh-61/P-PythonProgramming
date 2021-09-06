var = True   # to run the program i used var true

while var:      # used to so that i can change var to come out of the program
    if var:

        print("welcome to the treasure island"'\n'"your mission is to find the treasure")
        direction = input("you are at a cross road, Where do you want to go? type 'left' or 'right': ").lower()
        if direction == 'right':
            print("Game Over")
            var = False
            xyz = input(print("do you want to play again. type 'yes' or 'no'"))
            if xyz == 'yes':
                var = True  # in the if else statement i wanted to give user an another chance
            else:
                print("thank you for your time")

        elif direction == 'left':
            print("you came to a lake, there is an island in the middle of the lake")
            mode_of_motion = input("type 'wait' to wait for the boat. type 'swim' to swim across: ").lower()
            if mode_of_motion == 'swim':
                print("Game Over")
                var = False
                xyz = input(print("do you want to play again. type 'yes' or 'no'"))
                if xyz == 'yes':
                    var = True  # in the if else statement i wanted to give user an another chance
                else:
                    print("thank you for your time")
            else:
                print("you have reached the island unharmed")
                doors = input("there is a house with 3 doors.which color door do you choose? red,blue, or yellow : ").lower()
                if doors == 'red':
                    print("there is a dragon in the room!, Game Over")
                    var = False
                elif doors == 'blue':
                    print("You have entered in a room full of beasts!, Game Over")
                    var = False
                else:
                    print('you win!')
                    var = False
        else:
            print("you have enter wrong direction, choose again")
            xyz = input(print("do you want to play again. type 'yes' or 'no'"))
            if xyz == 'yes':
                var = True
            else:
                print("thank you for your time")
    else:   # when var is false it runs this statement and give user another chance or it can exit from the game
        xyz = input(print("do you want to play again. type 'yes' or 'no'"))
        if xyz == 'yes':
            var = True
        else:
            print("thank you for your time")
