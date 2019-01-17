import csv
import pprint
import sys, os
sys.path.append(os.path.abspath(os.path.join('')))


basefolder = os.path.join("HelperCode","FunctionFiles")

with open(os.path.join(basefolder, 'pokemontypes.csv'), mode='r') as infile:
    reader = csv.DictReader(infile)
    dicout = {}
    for row in reader:
        dicout.setdefault(row['move'], dict())
        dicout[row['move']].setdefault(row['target'], int())
        dicout[row['move']][row['target']] = int(row['damage_factor'])
        


pprint.pprint(dicout)
dicfile = 'elements.py'
dicname = 'ElementEffectiveness'

with open(os.path.join(basefolder,dicfile), "w+") as filename:
    filename.write(dicname + " = ")
    pprint.pprint(dicout, stream=filename)