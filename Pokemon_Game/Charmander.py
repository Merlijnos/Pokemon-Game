from Pokemon import Pokemon
from PokemonType import PokemonType

class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", "Fire", "Water")

    def battle_cry(self):
        return self.nickname + "!"