class prey:
    def flee(self):
        print("this animal is fleeing")

class predator:
    def hunt(self):
        print("this animal is hunting")

class rabid(prey):
    pass

class hawk(prey):
    pass

class fih(prey, predator):
   pass

rabid = rabid()
hawk = hawk()
fih = fih()

rabid.flee()