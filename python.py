class Dog:
    def __init__(self,name, breed):
        self.name = name
        self.breed = breed
    def blaf(self):
        print("woof")    

anton = Dog("Anton", "Bulldog")        

print(anton.name)

Dog.color = "red"

anton.color = "gold"

print(anton.color)

bello =Dog("bello", "Poodle")

bello.blaf()