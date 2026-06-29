class Superhero:
    def __init__(self, name, strength, speed, fly):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.fly = fly

    def __str__(self):
        if self.fly:
            flying = "is able to fly"
        else:
            flying = "is NOT able to fly"
        return f"{self.name} has {self.strength} strength, {self.speed} speed {flying}\n"

class bobCatMan(Superhero):
    def perform_ability(self):
        print(f"{self.name} uses his paws to rip your face off\n")

class Spiderman(Superhero):
    def perform_ability(self):
        print(f"{self.name} uses his webs to hand enemys\n")

bob_man = bobCatMan("BobCatMan", 1000, 9, False)
spider_man = Spiderman("Spiderman", 100000, 10000, True)

print(bob_man)
print(spider_man)

bob_man.perform_ability()
spider_man.perform_ability()