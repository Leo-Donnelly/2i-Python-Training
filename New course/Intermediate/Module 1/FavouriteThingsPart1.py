def favourite_things(*args):

    favourite_things = args

    for x, i in enumerate(favourite_things):
        if i.endswith("s"):
            verb = "are"
        else:
            verb = "is"

        if x == 0:
            print("One of my favourite things "+verb+" "+i)
        else:
            print("Another of my favourite things "+verb+" "+i)

    print("These are " + str(len(favourite_things))+ "of my favourite things")
        



favourite_things("chocolate", "videogames", "holidays", "relaxing")