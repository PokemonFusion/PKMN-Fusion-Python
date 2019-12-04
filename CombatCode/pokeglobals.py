import copy
from CombatCode.movesdex import BattleMovedex
from CombatCode.itemsdex import BattleItems


def keycheck(dictionary, subdictionary, key) -> object:
	if key in dictionary[subdictionary]:
		return dictionary[subdictionary][key]
	else:
		return None


class Result:
	def __init__(self):
		self.debug = dict()
		self.fainted = list()
		self.text = ""


class Items:

	def __init__(self, item: str):
		def itemcheck(key):
			return keycheck(BattleItems, item, key)

		self.desc = itemcheck("desc")
		self.gen = itemcheck("gen")
		self.id = itemcheck("id")
		self.megaEvolves = itemcheck("megaEvolves")
		self.megaStone = itemcheck("megaStone")
		self.name = itemcheck("name")
		self.num = itemcheck('num')
		self.onTakeItem = itemcheck('onTakeItem')
		self.spritenum = itemcheck('spritenum')
		self.forcedForme = itemcheck('forcedForme')
		self.rawData = BattleItems[item]


class Moves:

	def __init__(self, move: str):
		def movecheck(key):
			return keycheck(BattleMovedex, move, key)

		self.num = movecheck("num")
		self.accuracy = movecheck("accuracy")
		self.basePower = movecheck("basePower")
		self.category = movecheck("category")
		self.desc = movecheck("desc")
		self.shortDesc = movecheck("shortDesc")
		self.id = movecheck("id")
		self.name = movecheck("name")
		self.pp = movecheck("pp")
		self.priority = movecheck("priority")
		self.flags = movecheck("flags")
		self.secondary = movecheck("secondary")
		self.self = movecheck("self")
		self.target = movecheck("target")
		self.type = movecheck("type")
		self.zMovePower = movecheck("zMovePower")
		self.contestType = movecheck("contestType")
		self.multihit = movecheck("multihit")
		self.boosts = movecheck("boosts")
		self.isViable = movecheck("isViable")
		self.isZ = movecheck("isZ")
		self.onHit = movecheck("onHit")
		self.onModifyMove = movecheck("onModifyMove")
		self.critRatio = movecheck("critRatio")
		self.rawData = BattleMovedex[move]

	def calculateBasePower(self, datadic: dict) -> int:
		"""
		you'll need to check basePowerCallback and onBasePower
		"""
		calc = BattleMovedex[self.name.lower()].get('basePowerCallback', None)
		if calc is None:
			calc = BattleMovedex[self.name.lower()].get('onBasePower', None)

		if calc is None:
			return self.basePower
		else:
			return calc(datadic)

	def __repr__(self):
		return "{}. {}".format(self.num, self.name)

