travel_destinations = {}

def add_destination(name, info):
    travel_destinations[name] = info
    print("Destination added with key:value pair as \n", name, ":", info)

paris = {
    "country": "Paris",
    "population_millions": "2.1",
    "landmarks": ["Eifel tower", "Lourve Musem", " Notre-Dam"]
}

Tokyo = {
    "country": "Tokyo",
    "population_millions": "5.4",
    "landmarks": ["Pikachu", "Houses"]
}

add_destination("Paris", paris)
add_destination("Tokyo", Tokyo)