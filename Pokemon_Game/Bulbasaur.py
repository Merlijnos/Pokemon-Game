from Pokemon import Pokemon
from PokemonType import PokemonType

class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur", "Grass", "Fire")

    def battle_cry(self):
        return self.nickname + "!"