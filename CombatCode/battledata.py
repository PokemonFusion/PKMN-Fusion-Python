import CombatCode.pokeglobals as pglobals


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
    pass


class DeclareAttack:
    def __init__(self, target, move: pglobals.Moves):
        self.target = target #target is the position value
        self.move = move


class TurnInit:
    def __init__(self, switch=None, attack: DeclareAttack = None, item=None, run=None, recharge=None):
        # if switching a pokemon, put in the team position of the pokemon switching to
        self.switch = switch
        self.attack = attack  # if attacking, use a DeclareAttack here
        self.item = item  # if using an item, put the key here
        self.run = run  # if trying to run away, make True
        self.recharge = recharge  # if pokemon has to recharge, make True


class Pokemon:  # may remove this because of it being made somewhere else.
    pass
