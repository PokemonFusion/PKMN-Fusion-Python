import csv
import pprint
import sys, os
sys.path.append(os.path.abspath(os.path.join('')))


pokenames = {
    'nidoran-f' : "nidoranf",
    'nidoran-m' : "nidoranm",
    'mr-mime' : 'mrmime',
    'ho-oh': 'hooh',
    'deoxys-normal': 'deoxys',
    'wormadam-plant': 'wormadam',
    'mime-jr': 'mimejr',
    'porygon-z': 'porygonz',
    'giratina-altered' : 'giratina',
    'shaymin-land' : 'shaymin',
    'basculin-red-striped' : 'basculin',
    'darmanitan-standard':'darmanitan',
    'tornadus-incarnate': 'tornadus',
    'landorus-incarnate' : 'landorus',
    'keldeo-ordinary' : 'keldeo',
    'meloetta-aria' : 'meloetta',
    'meowstic-male' : 'meowstic',
    'aegislash-shield' : 'aegislash',
    'pumpkaboo-average' : 'pumpkaboo',
    'gourgeist-average' : 'gourgeist'

} #use this dictionary to change the names to what we have in the dictionary. Add new ones as needed.

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