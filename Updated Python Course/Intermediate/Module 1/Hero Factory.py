class superhero:
    def __init__(self, name, strength, speed, can_fly):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.can_fly = can_fly

    def perform_ability(self):
        if self.can_fly:
            print(f"{self.name} is flying in the sky at a speed of {self.speed}")
        else:
            print(f"{self.name} is not able to fly.. oh well")

    def __str__(self):
        return f"{self.name} (Strength: {self.strength}, Speed: {self.speed})"

class Superman(superhero):
    def perform_ability(self):
        return super().perform_ability()
    
class Batman(superhero):
    def perform_ability(self):
        print(f"{self.name} is not able to fly but he can turn into a bat!!!")

Superman = Superman("Superman", strength=100, speed=100000, can_fly=True)
Batman = Batman("Batman", strength=5000000, speed=10, can_fly=False)

Superman.perform_ability()
Batman.perform_ability()

print(Superman)
print(Batman)