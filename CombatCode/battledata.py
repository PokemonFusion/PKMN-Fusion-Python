import CombatCode.pokemon as pokemon
import CombatCode.pokeglobals as pglobals
import random


class BattleData:

    def __init__(self):
        # These will eventually be classes
        self.teams = {"A": Teams(), "B": Teams()}
        self.battle = Battle()
        self.turndata = TurnData()


class Teams:
    pass


class Battle:
    pass

class TurnData:
    def __init__(self, positions=None):
        self.positions = positions


class DeclareAttack:
    def __init__(self, target, move: pglobals.Moves):
        self.target = target  # target is the position value
        self.move = move


class TurnInit:
    def __init__(self, switch=None, attack: DeclareAttack = None, item=None, run=None, recharge=None):
        # if switching a pokemon, put in the team position of the pokemon switching to
        self.switch = switch
        self.attack = attack  # if attacking, use a DeclareAttack here
        self.item = item  # if using an item, put the key here
        self.run = run  # if trying to run away, make True
        self.recharge = recharge  # if pokemon has to recharge, make True


# may remove this because of it being made somewhere else.
class Pokemon(pokemon.Pokemon):

    def __init__(self, ot, team, slot, species='missingno', nickname=None, gender=None, isEgg=False, level=1,
                 ability=random.choice(['0', '1'])):
        super().__init__(ot, species=species, nickname=nickname,
                         gender=gender, isEgg=isEgg, level=level, ability=ability)
        self.team = team
        self.slot = slot

    def getPosition(self):
        return self.team + str(self.slot)


class PositionData:
    def __init__(self, pokedata: Pokemon = None):
        self.pokemon = pokedata
