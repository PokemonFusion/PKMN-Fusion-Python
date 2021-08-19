from movesdex import BattleMovedex as dex
from pprint import pprint

dicnamekey = {}

for key in dex:
	dicnamekey[key] = dex[key]["num"]

dicnumkey = {}

for key in dicnamekey:
	dicnumkey[dicnamekey[key]] = key

pprint(dicnumkey)
