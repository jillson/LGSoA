#small wrapper around namegen

import os

from name_gen.namegen import NameGen as rNameGen

class NameGen:
    def __init__(self,language="elven.txt",randomGen = None):
        self.rng = rNameGen(os.path.join(os.path.dirname(__file__),"name_gen","Languages",language), randomGen)
    def getName(self):
        return self.rng.gen_word()

