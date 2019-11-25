import CombatCode.pokemon as pokemon
import CombatCode.pokeglobals as pglobals
import random


class BattleData:

	def __init__(self, TeamA, TeamB):
		# These will eventually be classes
		self.teams = {"A": TeamA, "B": TeamB}
		self.battle = Battle()
		self.turndata = TurnData(self.teams)


class Team:

	def __init__(self, trainer, pokemon_list: list = []):
		self.trainer = trainer
		self.slot1 = None
		self.slot2 = None
		self.slot3 = None
		self.slot4 = None
		self.slot5 = None
		self.slot6 = None

		pokelist = [None, None, None, None, None, None]
		for x in range(len(pokemon_list)):
			if x == 6:
				break
			pokelist[x] = pokemon_list[x]

		self.slot1, self.slot2, self.slot3, self.slot4, self.slot5, self.slot6 = \
			pokelist[0], pokelist[1], pokelist[2], pokelist[3], pokelist[4], pokelist[5]

	def returnlist(self) -> list:
		pokelist = [None, None, None, None, None, None]

		pokelist[0], pokelist[1], pokelist[2], pokelist[3], pokelist[4], pokelist[5] =\
			self.slot1, self.slot2, self.slot3, self.slot4, self.slot5, self.slot6

		return pokelist

	def swapslots(self, pos1: int, pos2: int) -> str:
		def fixposnum(pos: int) -> int:
			if pos < 1:
				return 1
			elif pos > 6:
				return 6
			else:
				return pos
		pos1 = fixposnum(pos1)
		pos2 = fixposnum(pos2)

		slotdic = {1: self.slot1,
		           2: self.slot2,
		           3: self.slot3,
		           4: self.slot4,
		           5: self.slot5,
		           6: self.slot6}

		result = f"Switching positions {pos1}. {slotdic[pos1].getName()} with {pos2}. {slotdic[pos2].getName()}."

		slotdic[pos1], slotdic[pos2] = slotdic[pos2], slotdic[pos1]

		self.slot1, self.slot2, self.slot3, self.slot4, self.slot5, self.slot6 = \
			slotdic[1], slotdic[2], slotdic[3], slotdic[4], slotdic[5], slotdic[6]

		return result

	def callslot(self, pos: int) -> pokemon:

		if pos < 1:
			pos = 1
		if pos > 6:
			pos = 6

		slotdic = {1: self.slot1,
		           2: self.slot2,
		           3: self.slot3,
		           4: self.slot4,
		           5: self.slot5,
		           6: self.slot6}

		return slotdic[pos]


class Battle:
	def __init__(self, battletype=1):
		self.turn = 0  # start at 0, but at the start of the turn increment by one.
		self.battletype = battletype  # current valid input, 1, 2, 3, as in how many pokemon out per team


class TurnData:
	def __init__(self, teams: dict = None, teamslots: int = 1):
		self.positions = {}  # PositionData class as dictionary

		def populateslots(teamname, teamclass):
			count = 0
			for poke in teamclass.returnlist():
				if count >= teamslots:
					return
				posname = teamname + str(count + 1)
				if poke is not None:
					if poke.hp > 0:
						self.positions[posname] = PositionData(poke)
						count += 1
						continue
			if count < teamslots:
				while count < teamslots:
					posname = teamname + str(count + 1)
					self.positions[posname] = PositionData()
					count += 1

		for team, members in teams.items():
			populateslots(team, members)


class DeclareAttack:
	def __init__(self, target: str, move: pglobals.Moves):
		self.target = target  # target is the position value
		self.move = move

	def __repr__(self):
		return "{} -> {}".format(self.move.name, self.target)


# This class is what will store the turn initialization data, letting you know what the pokemon in that position is
# doing in that turn.
class TurnInit:
	def __init__(self, position: str = None, switch=None, attack: DeclareAttack = None, item=None, run=None, recharge=None):
		# if switching a pokemon, put in the team position of the pokemon switching to
		self.switch = switch
		self.attack = attack  # if attacking, use a DeclareAttack here
		self.item = item  # if using an item, put the key here
		self.run = run  # if trying to run away, make True
		self.recharge = recharge  # if pokemon has to recharge, make True
		# self.position = position

	def getTarget(self):
		if self.attack is None:
			#return self.position
			return None
		else:
			return self.attack.target


class Pokemon(pokemon.Pokemon):
	# may remove this because of it being made somewhere else.

	def __init__(self, ot, species='missingno', nickname=None, gender=None, isEgg=False, level=1,
	             ability=random.choice(['0', '1'])):
		super().__init__(ot, species=species, nickname=nickname,
		                 gender=gender, isEgg=isEgg, level=level, ability=ability)
		# self.turninit = None  # TurnInit Class
		self.tempvals = {}


class PositionData:
	def __init__(self, pokedata: Pokemon = None):
		self.pokemon = pokedata  # pokemon class
		self.turninit = TurnInit()

	def getTarget(self):
		return self.turninit.getTarget()  # different getTarget method

	def getAction(self):
		if self.turninit.attack:
			return self.turninit.attack.move
		# TODO: Add the other actions here later
		return None

	def declareAttack(self, target, move):
		# This method assumes the target and the move are valid
		self.turninit = TurnInit(attack=DeclareAttack(target, pglobals.Moves(move)))

	def declareSwitch(self, slotswitch):
		# This method assumes the slotswitch is valid
		self.turninit = TurnInit(switch=slotswitch)

	def removeDeclare(self):
		# This method removes all declare values.
		self.turninit = TurnInit()