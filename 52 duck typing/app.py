class animal:
    alive = True

class dog(animal):
    def speak(self):
        print("woof")

class cat(animal):
    def speak(self):
        print("meow")

class car:
    alive = False
    def speak(self):
        print("honk")

animals = [dog(), cat(), car()]

for animal in animals:
    animal.speak()
    print(animal.alive)