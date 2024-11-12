from Pokemon import Pokemon
from PokemonType import PokemonType

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", "Water", "Leaf")

    def battle_cry(self):
        return self.nickname + "!"