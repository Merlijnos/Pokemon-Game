from Battle import Battle

class Arena:
    total_rounds = 0
    total_battles = 0

    @staticmethod
    def fight_battle(trainer1, trainer2):
        battle = Battle(trainer1, trainer2)
        battle.start_battle()
        Arena.total_battles += 1
        if len(trainer1.belt) == 0 and len(trainer2.belt) > 0:
            return trainer2
        elif len(trainer2.belt) == 0 and len(trainer1.belt) > 0:
            return trainer1
        elif len(trainer1.belt) == 0 and len(trainer2.belt) == 0:
            return None
        else:
            return battle.get_winner()

    @staticmethod
    def increment_rounds():
        Arena.total_rounds += 1

    @staticmethod
    def get_scoreboard():
        return {
            'total_rounds': Arena.total_rounds,
            'total_battles': Arena.total_battles
        }