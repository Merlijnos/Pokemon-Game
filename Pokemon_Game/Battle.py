import random

class Battle:
    def __init__(self, trainer1, trainer2):
        self.trainer1 = trainer1
        self.trainer2 = trainer2
        self.winner_of_last_round = None

    def conduct_round(self):
        from Arena import Arena  # Move the import statement here

        pokeball1 = random.choice(self.trainer1.belt)
        pokeball2 = random.choice(self.trainer2.belt)
        pokemon1 = pokeball1.throw()
        pokemon2 = pokeball2.throw()

        print(f"{self.trainer1.name} throws a pokeball!")
        print(f"{pokemon1.nickname} says: {pokemon1.battle_cry()}")
        print(f"{self.trainer2.name} throws a pokeball!")
        print(f"{pokemon2.nickname} says: {pokemon2.battle_cry()}")

        if pokemon1.strength == pokemon2.weakness:
            self.winner_of_last_round = self.trainer1
            self.trainer2.belt.remove(pokeball2)
            print(f"{pokemon1.nickname} wins the round because {pokemon1.nickname}'s strength ({pokemon1.strength}) is {pokemon2.nickname}'s weakness ({pokemon2.weakness}). {pokemon2.nickname} is defeated!")
        elif pokemon2.strength == pokemon1.weakness:
            self.winner_of_last_round = self.trainer2
            self.trainer1.belt.remove(pokeball1)
            print(f"{pokemon2.nickname} wins the round because {pokemon2.nickname}'s strength ({pokemon2.strength}) is {pokemon1.nickname}'s weakness ({pokemon1.weakness}). {pokemon1.nickname} is defeated!")
        else:
            if self.winner_of_last_round == self.trainer1:
                self.trainer2.belt.remove(pokeball2)
                print(f"{pokemon1.nickname} wins the round because it won the previous round. {pokemon2.nickname} is defeated!")
            elif self.winner_of_last_round == self.trainer2:
                self.trainer1.belt.remove(pokeball1)
                print(f"{pokemon2.nickname} wins the round because it won the previous round. {pokemon1.nickname} is defeated!")
            else:
                self.trainer1.belt.remove(pokeball1)
                self.trainer2.belt.remove(pokeball2)
                print("It's a draw! Both Pokemon are returned to their Pokeballs.")

        print(f"{self.trainer1.name} has {len(self.trainer1.belt)} Pokeballs left.")
        print(f"{self.trainer2.name} has {len(self.trainer2.belt)} Pokeballs left.")

        # Increment the total rounds after each round
        Arena.increment_rounds()

    def start_battle(self):
        while len(self.trainer1.belt) > 0 and len(self.trainer2.belt) > 0:
            self.conduct_round()

    def get_winner(self):
        if len(self.trainer1.belt) > len(self.trainer2.belt):
            return self.trainer1
        elif len(self.trainer2.belt) > len(self.trainer1.belt):
            return self.trainer2
        else:
            return None