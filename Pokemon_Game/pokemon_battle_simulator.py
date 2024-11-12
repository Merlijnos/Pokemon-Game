import self

from Charmander import Charmander
from Squirtle import Squirtle
from Bulbasaur import Bulbasaur
from Trainer import Trainer
from Pokeball import Pokeball
from Arena import Arena


class PokemonBattleSimulator:
    def __init__(self):        self.trainer1 = None
    self.trainer2 = None

    def start(self):
        while True:  # Start of the loop
            print("Welcome to the Pokemon Battle Simulator!")
            trainer1_name = input("Enter a name for the first trainer: ")
            trainer2_name = input("Enter a name for the second trainer: ")

            trainer1_belt = [Pokeball(Charmander()), Pokeball(Squirtle()), Pokeball(Bulbasaur()),
                             Pokeball(Charmander()), Pokeball(Squirtle()), Pokeball(Bulbasaur())]
            trainer2_belt = [Pokeball(Charmander()), Pokeball(Squirtle()), Pokeball(Bulbasaur()),
                             Pokeball(Charmander()), Pokeball(Squirtle()), Pokeball(Bulbasaur())]

            self.trainer1 = Trainer(trainer1_name, trainer1_belt)
            self.trainer2 = Trainer(trainer2_name, trainer2_belt)

            winner = Arena.fight_battle(self.trainer1, self.trainer2)
            if winner is not None:
                print(f"The winner is {winner.name}!")
            else:
                print("The battle is a draw!")

            scoreboard = Arena.get_scoreboard()
            print(f"Total rounds fought: {scoreboard['total_rounds']}")
            print(f"Total battles fought: {scoreboard['total_battles']}")

            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != "yes":
                break  # End of the loop

        print("Thank you for playing the Pokemon Battle Simulator!")


if __name__ == "__main__":
    simulator = PokemonBattleSimulator()
    simulator.start()
