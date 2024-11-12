class Trainer:
    MAX_POKEBALLS = 6

    def __init__(self, name, belt):
        if len(belt) > Trainer.MAX_POKEBALLS:
            raise Exception("Too many Pokeballs!")
        self.__name = name
        self.__belt = belt

    @property
    def name(self):
        return self.__name

    @property
    def belt(self):
        return self.__belt

    def throw_pokeball(self, pokeball):
        if pokeball.pokemon is not None:
            return pokeball.throw()
        else:
            return None

    def return_pokeball(self, pokeball):
        return pokeball.return_pokemon()