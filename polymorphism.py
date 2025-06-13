class cricket:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def printdetails(self):
            print("lets play cricket")

class football:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def printdetails(self):
        print("lets play football")

class muaythai:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def printdetails(self):
        print("lets play muay thai")

c1 = cricket("KL", "batsman")
f1 = football("Ronaldo", "forward")
m1 = muaythai("Nong-O", "fighter")

for x in (c1, f1, m1):
    x.printdetails()