import CombatCode.pokemon as pokemon
import CombatCode.pokeglobals as pglobals
import random


class BattleData:

	def __init__(self, trainerA, teamAlist, trainerB, teamBlist ):
		# These will eventually be classes
		self.teams = {"A": Team(trainerA, teamAlist), "B": Team(trainerB, teamBlist)}
		self.battle = Battle()
		self.turndata = TurnData()


class Team:

	def __init__(self, trainer, pokemon_list: list = []):
		self.trainer = trainer
		self.pokedict = {}
		count = 0

		while pokemon_list.count() > 0:
			count += 1
			self.pokedict["slot" + str(count)] = pokemon_list.pop(0)
			if count == 6:
				break


class Battle:
	def __init__(self, battletype):
		self.turn = 0  # start at 0, but at the start of the turn increment by one.
		self.battletype = battletype  # current valid input, 1, 2, 3, as in how many poekmon out per team


class TurnData:
	def __init__(self, positions: dict = None):
		self.positions = positions  # PositionData class


class DeclareAttack:
	def __init__(self, target: str, move: pglobals.Moves):
		self.target = target  # target is the position value
		self.move = move

	def __repr__(self):
		return "{} -> {}".format(self.move.name, self.target)


# This class is what will store the turn initialization data, letting you know what the pokemon in that position is
# doing in that turn.
class TurnInit:
	def __init__(self, position: str, switch=None, attack: DeclareAttack = None, item=None, run=None, recharge=None):
		# if switching a pokemon, put in the team position of the pokemon switching to
		self.switch = switch
		self.attack = attack  # if attacking, use a DeclareAttack here
		self.item = item  # if using an item, put the key here
		self.run = run  # if trying to run away, make True
		self.recharge = recharge  # if pokemon has to recharge, make True
		self.position = position

	def getTarget(self):
		if self.attack is None:
			return self.position
		else:
			return self.attack.target


class Pokemon(pokemon.Pokemon):
	# may remove this because of it being made somewhere else.

	def __init__(self, ot, team, slot, species='missingno', nickname=None, gender=None, isEgg=False, level=1,
	             ability=random.choice(['0', '1'])):
		super().__init__(ot, species=species, nickname=nickname,
		                 gender=gender, isEgg=isEgg, level=level, ability=ability)
		self.team = team
		self.slot = slot
		# self.turninit = None  # TurnInit Class
		self.tempvals = {}

	def getPosition(self):
		return self.team + str(self.slot)


class PositionData:
	def __init__(self, pokedata: Pokemon = None):
		self.pokemon = pokedata  # pokemon class

	def getTarget(self):
		return self.turninit.getTarget()  # different getTarget method

	def getAction(self):
		if self.turninit.attack:
			return self.turninit.attack.move
		# TODO: Add the other actions here later
		return None
