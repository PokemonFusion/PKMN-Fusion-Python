import pprint
import sys, os
sys.path.append(os.path.abspath(os.path.join('')))

from CombatCode.pokemondex import BattlePokedex as dex
from CombatCode.pokemonCatchData import pokemonCatchData as catchdata


def merge(a,b, path=None):
    "merges b into a"
    if path is None: path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge(a[key], b[key], path + [str(key)])
            elif a[key] == b[key]:
                pass # same leaf value
            else:
                raise Exception('Conflict at %s' % '.'.join(path + [str(key)]))
        else:
            a[key] = b[key]
    return a

dicout = merge(dex, catchdata)

basefolder = os.path.join("HelperCode","FunctionFiles")
dicfile = 'pokemonCombinedDex.py'
dicname = 'BattlePokedex'

with open(os.path.join(basefolder,dicfile), "w+", encoding="utf-8") as filename:
    filename.write(dicname + " = ")
    pprint.pprint(dicout, stream=filename)