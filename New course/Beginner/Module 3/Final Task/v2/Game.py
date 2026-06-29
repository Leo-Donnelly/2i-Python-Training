from TheGreatMorningScramble import choose_room

def game():
    print("You have lost the key to your front door. You need to search for it so you can get to work in time")

    while True:
        print("\n What room do you want to search first? \n Living Room \n Bedroom \n Garage")
        room = input("").lower

        if room not in ["living room", "bedroom", "garage"]:
            print("That isnt a room, Try again!")
            continue

        result, found = choose_room.roomChoice(room)
        print(result)

        if found:
            print("Now get to work!!!!")
            break

game()