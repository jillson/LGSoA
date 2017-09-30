
class Town:
    def __init__(self,name="Nome"):
        self.name = name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name


class TownFactory:
    def __init__(self,nameGen):
        self.nameGen = nameGen
        self.towns = {}
    def createTown(self):
        for _ in range(10):
            n = self.nameGen.getName()
            if not self.towns.get(n):
                t = Town(n)
                self.towns[n] = t
                return t
        n = "New " + n
        while self.towns.get(n):
            n = "New " + n
        t = Town(n)
        self.towns[n] = t
        return t
