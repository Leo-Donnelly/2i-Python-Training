def make_toy(integer):
    for x in range (1, integer + 1):
        print("Building toy!")
        yield f"Toy #{x} is ready to be wrapped and put into the sleigh!"

toy = make_toy(5)

for x in range(5):
    print(next(toy))
