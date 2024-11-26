import random
class Animal:
    _cords = [0, 0, 0]
    def __init__(self, name, _cords):
        self.name = name
        self.live = True
        self.sound = None
    speed = 10
    def move(self, dx, dy, dz):
        super().__init__(dx, dy, dz)
        self._cords += dx
        self._cords += dy
        self._cords += dz
        if dz < 0:
            print("It's too deep, i can't dive :(")
    def get_cords(self):
        print(f"X: {dx} Y: {dy} Z: {dz}")
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")
    def speak(self):
        print(self.sound)
    _DEGREE_OF_DANGER = 0

class Bird(Animal):
    beak = True
    def lay_eggs(self):
        print(f"Here are(is) {random.choice([1, 2, 3, 4])} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    #def dive_in(self, dz):

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = "Click-click-click"

db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()