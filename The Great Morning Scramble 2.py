def choose_room():
    print("You are currently in the hallway. What room would you like to go to?")
    print("Kitchen\nLivingroom\nBathroom\nBedroom\nGarage")
    roomChoice = input("")
    return roomChoice  

def start_room(roomChoice):
    print("You have choose to search the", roomChoice)
    print("What would you like to do?")
    choice = input("Search the room, Leave the room or Give up \n")
    if choice == "Search the room":
        keyFound = search_room(roomChoice)
        if keyFound == True:
            print("You have found the key and are able to get to work on time!")
            exit()
        else:
            print("You have lost your key and are going to be very late for work. You will also be put on the bosses email list.")
            exit()
    elif choice == "Leave the room":
        print("You have left the room and are now back in the hallway")
        choose_room()
    elif choice == "Give up":
        print("You gave up, your gonna get a fair email from your boss!")
        exit()

def Search_Room(roomChoice):
    if roomChoice == "Kitchen":
         keyFound = False
    elif roomChoice == "Livingroom":
         keyFound = False
    elif roomChoice == "Bathroom":
         keyFound = False
    elif roomChoice == "Bedroom":
         keyFound = False
    else:
         keyFound = True

    return keyFound

    
def Find_Key():
    print("Well done you have found the key to leave the house, \n you will no longer be put on the bosses list.")



def main():
    roomChoice = choose_room()
    start_room(roomChoice)



main();