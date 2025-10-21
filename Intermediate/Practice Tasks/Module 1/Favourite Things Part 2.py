def favourite_things(*args, **kwargs):

    top_favourites = kwargs
    other_favourites = args

    print("Here are my top " + str(len(top_favourites)) + " favourite things")
    print("---")

    for position, top_item in top_favourites.items():
        print(position + ": " + top_item)

    print("---")
    print("Some of my other favourite things are: ")

    for index, other_item in enumerate(other_favourites):
        if index == len(other_favourites) -1:
            print("and "+ other_item)
        else:
            print(other_item)


favourite_things("Cars", "Food", "Beers", First="Motorcycling", Second="Driving cars", Third="Going on holibobs")