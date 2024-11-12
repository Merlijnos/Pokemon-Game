from abc import ABC, abstractmethod

class Pokemon(ABC):
    def __init__(self, nickname, strength, weakness):
        self.__nickname = nickname
        self.__strength = strength
        self.__weakness = weakness

    @abstractmethod
    def battle_cry(self):
        pass

    @property
    def nickname(self):
        return self.__nickname

    @property
    def strength(self):
        return self.__strength

    @property
    def weakness(self):
        return self.__weakness