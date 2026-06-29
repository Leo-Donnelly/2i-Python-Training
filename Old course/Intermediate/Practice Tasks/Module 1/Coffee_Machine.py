def add_milk(func):
    def wrapper(*args, **kwargs):
        print("You add milk")
        func(*args, **kwargs)
    return wrapper

def add_sugar(func):
    def wrapper(*args, **kwargs):
        print("You add sugar")
        func(*args, **kwargs)
    return wrapper

@add_milk
@add_sugar
def get_coffee(type_of_coffee):
    print (f"Here is your {type_of_coffee}, enjoy!")

get_coffee("Cappuccino")


