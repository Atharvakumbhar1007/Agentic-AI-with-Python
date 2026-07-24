class Chaicup:
    size = 150 #ml
    
    def describe(self):
        return f"A {self.size}ml Chai cup"
    
cup = Chaicup()
print(cup.describe())
print(Chaicup.describe())

cup_two = Chaicup()
print(cup_two.describe())
print(Chaicup.describe(cup_two))