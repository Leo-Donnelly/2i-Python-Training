def choose_room():
    print("What room do you want to search first? \n Living Room \n Bedroom \n Garage")
    roomChoice = input("").lower()
    while roomChoice not in ["living room", "bedroom", "garage"]:
        print("That isnt a room! Try again")
        roomChoice = input("").lower()
    start_room(roomChoice)

def start_room(roomChoice):
    print("Do you want to search", roomChoice+"?")
    SearchOrNot = input("").lower()
    if SearchOrNot == "no":
        print("Okay, your going to need to search another room!!")
        choose_room()
        return
    
    if roomChoice == "living room":
        find_key()
    else:
        print("The key isnt in here try again!")
        choose_room()

def find_key():
    print("You have found the key! Now GET TO WORK!!!!")

print("You have lost your key! You have to search rooms to find it or you will go on to the strongly worded email list")
choose_room()