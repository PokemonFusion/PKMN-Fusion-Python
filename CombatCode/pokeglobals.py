import copy
from CombatCode.movesdex import BattleMovedex
from CombatCode.itemsdex import BattleItems
from CombatCode.abilitiesdex import BattleAbilities


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
		self.basePowerCallback = movecheck("basePowerCallback")
		self.onBasePower = movecheck("onBasePower")

	def calculateBasePower(self, **bvalues) -> int:
		"""
		you'll need to check basePowerCallback and onBasePower
		"""
		calc = self.basePowerCallback
		if calc is None:
			calc = self.onBasePower

		if calc is None:
			return self.basePower
		else:
			return calc(**bvalues, basepower=self.basePower)

	def __repr__(self):
		return "{}. {}".format(self.num, self.name)


class Abilities:
	def __init__(self, ability: str):
		def abilitycheck(key):
			return keycheck(BattleAbilities, ability.lower(), key)

		self.num = abilitycheck("num")
		self.name = abilitycheck("name")
		self.isBreakable = abilitycheck("isBreakable")
		self.onModifyAtk = abilitycheck("onModifyAtk")
		self.onModifyAtkPriority = abilitycheck("onModifyAtkPriority")
		self.onModifySpA = abilitycheck("onModifySpA")
		self.onModifySpAPriority = abilitycheck("onModifySpAPriority")
		self.rating = abilitycheck("rating")
		self.onModifySpe = abilitycheck("onModifySpe")
		self.onHit = abilitycheck("onHit")
