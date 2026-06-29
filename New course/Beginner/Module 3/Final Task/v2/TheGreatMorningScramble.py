class choose_room:
    @staticmethod
    def roomChoice(room):
        room = room.lower()

        if room == "living room":
            return ("You win, You have found the key.. Now get to work!", True)
        elif room in ["bedroom", "garage"]:
            return ("No key here, search elsewhere!", False)
        else:
            return ("Thats not a room", False)