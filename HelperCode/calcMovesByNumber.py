from movesdex import BattleMovedex as dex
from pprint import pprint

dicnamekey = {}

for key in dex:
	if not dex[key].get("implemented", False):
		dicnamekey[key] = dex[key]["num"]

dicnumkey = {}

for key in dicnamekey:
	dicnumkey[dicnamekey[key]] = key

# remove the moves that won't be coded at all.
dicnumkey.pop(0)
dicnumkey.pop(1000)
count = 0
for x in range(1, 1000):
	if dicnumkey.get(x):
		print(f"{x}: '{dicnumkey[x]}'")
		count += 1
		if count == 10:
			break
