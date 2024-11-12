class Pokeball:
    def __init__(self, pokemon=None):
        self.__pokemon = pokemon

    @property
    def pokemon(self):
        return self.__pokemon

    def throw(self):
        if self.__pokemon is not None:
            return self.__pokemon
        else:
            return "The Pokeball is empty!"

    def return_pokemon(self):
        if self.__pokemon is not None:
            pokemon = self.__pokemon
            self.__pokemon = None
            return pokemon
        else:
            return "The Pokeball is already empty!"