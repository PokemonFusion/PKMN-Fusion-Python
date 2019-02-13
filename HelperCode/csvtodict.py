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
    'gourgeist-average' : 'gourgeist',
    'thundurus-incarnate' : 'thundurus'

} #use this dictionary to change the names to what we have in the dictionary. Add new ones as needed.

def renameFieldName(x: str):
    xsplit = x.split('_')
    for i in range(len(xsplit)):
        if i == 0:
            xsplit[i] = xsplit[i].lower()
        else:
            xsplit[i] = xsplit[i].title()
    return ''.join(xsplit)



basefolder = os.path.join("HelperCode","FunctionFiles")

with open(os.path.join(basefolder, 'pokemonCatchData.csv'), mode='r') as infile:
    reader = csv.DictReader(infile)
    dicout = {}
    #populate a list of field names
    fields = []
    for field in reader.fieldnames:
        fields.append(field)
    
    #make a dictionary of the renamed fields
    fieldDic = {}
    for field in fields:
        fieldDic[field] = renameFieldName(field)
    

    for row in reader:
        name = row[fields[0]]
        if name in pokenames:
            name = pokenames[name]
        dicout.setdefault(name, dict())
        for i in range(1, len(row)):
            dicout[name][fieldDic[fields[i]]] = int(row[fields[i]])
        # dicout[row['move']].setdefault(row['target'], int())
        # dicout[row['move']][row['target']] = int(row['damage_factor'])
        


#pprint.pprint(dicout)
dicfile = 'pokemonCatchData.py'
dicname = 'pokemonCatchData'

with open(os.path.join(basefolder,dicfile), "w+") as filename:
    filename.write(dicname + " = ")
    pprint.pprint(dicout, stream=filename)