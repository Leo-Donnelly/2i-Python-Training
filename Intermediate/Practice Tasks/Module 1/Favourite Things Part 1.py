def favourite_things(*args):

    favourite_list = args

    for index, item in enumerate(favourite_list):
        if item.endswith("s"):
            verb="are"
        else:
            verb="is"

        if index ==0:
            print("One of my favourite things " + verb + " "+item)
        else:
            print("Another one of my favourite things " + verb + " "+item)

    print("These are "+ str(len(favourite_list))+" of my favourite things")

favourite_things("Cars", "Food", "Beers", "Motorcycling")  