from __future__ import division

from random import Random

from generators.namegen import NameGen
from town import Town


class World:
    def __init__(self,
                 name="Default Name",
                 seed=None,
                 width=80,
                 height=80
    ):
        self.name = name
        self.random = Random()
        if seed:
            self.random.seed(seed)
        self.seed = seed
        self.width = width
        self.height = height
        self.size = width * height
        self.namegen = NameGen(randomGen=self.random)
        self.towns = [Town(name=self.namegen.getName()) for _ in range(max(self.size//10,1))]
        
        
    def getInitialData(self):
        return {"name":self.name,
                "seed":self.seed,
                "width":self.width,
                "height":self.height,
                "towns":self.towns
        }
        
            
        
if __name__ == "__main__":
    w = World()
    print w.getInitialData()
