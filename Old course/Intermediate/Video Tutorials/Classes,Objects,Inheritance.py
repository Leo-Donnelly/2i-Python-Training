class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along...")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")

my_car = Vehicle('BMW', '525D')

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Vauxhall', 'Corsa')

your_car.get_make_model()
your_car.moves()


class Airplane(Vehicle):
    def __init__(self, make, model, ISAO_id):
        super().__init__(make,model)
        self.ISAO_id = ISAO_id

    def moves(self):
        print("Flys along...")

class Lorry(Vehicle):
    def moves(self):
        print("Rolls along...")

class GolfCart(Vehicle):
    pass

cessna = Airplane('Cessna', '172', '532234LA')
Scania = Lorry('Scania', 'R Series')
GolfBuggy = GolfCart('Golf', 'Cart')

cessna.get_make_model()
cessna.moves()
Scania.get_make_model()
Scania.moves()
GolfBuggy.get_make_model()
GolfBuggy.moves()

print('\n \n')

for v in (my_car, your_car, cessna, Scania, GolfBuggy):
    v.get_make_model()
    v.moves()
    