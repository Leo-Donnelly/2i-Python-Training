def choose_room():
    print("You are currently in the hallway. What room would you like to go to?")
    print("Kitchen,\n Livingroom, \n Bathroom, \n Bedroom, \n Garage")
    roomChoice = input()
    return roomChoice


def start_room(roomchoice):
    print("You have choose to search the", roomchoice)
    print("What would you like to do?")
    choice = input("Search the room, Leave the room or Give up \n")

    
def find_key():
    print("Well done you have found the key to leave the house, \n you will no longer be put on the bosses list.")



def main():
    roomchoice = choose_room
    start_room(roomchoice)



main();