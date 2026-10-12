class animal:
    def __init__(self, name):
        self.name = name
        self.isAlive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class dog(animal):
    def speak(self):
        print("woof")

class cat(animal):
    def speak(self):
        print("meow")

class mouse(animal):
    def speak(self):
        print("squawk")


dog = dog("scooby")
cat = cat("garfield")
mouse = mouse ("mickey")

print(dog.name)
dog.eat()
cat.speak()