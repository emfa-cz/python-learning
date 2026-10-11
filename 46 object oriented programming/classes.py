
if __name__ != "__main__":
    class car:
        def __init__(self, model, year, colour, forSale):
            self.model = model
            self.year = year
            self.colour = colour
            self.forSale = forSale

        def drive(self):
            print(f"you drive the {self.colour} {self.model}")

        def stop(self):
            print(f"you stop the car {self.colour} {self.model}")
else:
    print("cannot run code directly")