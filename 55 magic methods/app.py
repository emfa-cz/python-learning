class book:
    def __init__(self, tit, auth, numPg):
        self.tit = tit
        self.auth = auth
        self.numPg = numPg

    def __str__(self):
        return f"{self.tit} by {self.auth}"

    def __eq__(self, oth):
        return self.tit == oth.tit and self.auth == oth.auth

    def __lt__(self, oth):
        return self.numPg < oth.numPg


book1 = book("the h", "jrr t", 310)
book2 = book("hp", "jkr", 310)
book3 = book("tl", "csl", 172)



print(book2)
print(book1 == book2)
print(book2 < book3)