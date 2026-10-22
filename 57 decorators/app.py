def addSprinkles(fun):
    def wrapper(*args, **kwargs):
        print("here is your ice cream with sprinkles:")
        fun(*args, **kwargs)
    return wrapper


def addFuck(fun):
    def wrapper(*args, **kwargs):
        print("you added fudge")
        fun(*args, **kwargs)
    return wrapper


@addSprinkles
@addFuck
def getIceCream(flavour):
    print(f"here is your {flavour} ice cream:")

getIceCream("vanilla")