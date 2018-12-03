"""This function is to be run on it's own.  This is used to remove the weirdness of function calls from importing
a javascript dictionary to python.
for the move return, you will have to fix the capitalization of the function, because return is a special function
This will need to be fixed in moves.py, the file name of Return.py, and __init__.py
"""

import sys, os
sys.path.append(os.path.abspath(os.path.join('')))
from CombatCode.moves import BattleMovedex
from CombatCode.abilities import BattleAbilities
from pprint import pprint

basefolder = os.path.join("HelperCode","FunctionFiles")
task = ""
workingfolder = ""
data = ""
tododata = ""
modulelist = []

def makedir(dir):
    try:
        os.mkdir(dir)
    except Exception:
        pass

def dicscan(dictionary : dict, masterkey : str = None):
    """Search for function then replace the string with a function call using eval()"""
    global data #this is global because of the recursion that happens
    global workingfolder
    global task
    global tododata
    global modulelist
    for key, val in dictionary.items():
        if masterkey == None:
            data = ""
        if isinstance(val,dict):
            if masterkey == None:
                dicscan(dictionary[key], key)
            else:
                dicscan(dictionary[key], masterkey)
        elif isinstance(val, str):
            if val.startswith("function ("):
                if data != "":
                    data += "\n\n"
                functionname = str(masterkey + "." + key)
                functionstring = val[0: val.find(')') + 1].replace("function", key)
                data += "def " + functionstring + ':\n\t"""' + val + '\n\t""" \n\tpass'
                dictionary[key] = "[deleteme]" + functionname + "[/deleteme]"
                tododata += "  ☐ " + functionname + "\n"
                modulelist.append(masterkey)
        
        if masterkey == None and data != "":
            with open(os.path.join(workingfolder, key + ".py"),"w+") as funfile:
                funfile.write(data)

def writenewdict(dictionary, dicname, dicfile):
    """write the new dictionary file"""
    global basefolder
    with open(os.path.join(basefolder,dicfile), "w+") as filename:
        filename.write("from " + task + " import * \n\n")
        filename.write(dicname + " = ")
        pprint(dictionary, stream=filename)

def writenewinit():
    """Write the new __init__.py file"""
    global modulelist, workingfolder
    with open(os.path.join(workingfolder,"__init__.py"), "w+") as init:
        init.write("__all__ = ")
        pprint(sorted(list(set(modulelist))), stream= init)

def fixdict(dicfile):
    """fix the dictionary file, removing the delete me parts"""
    global basefolder
    data = ""

    with open(os.path.join(basefolder,dicfile), "r") as filename:
        data = filename.read().replace("'[deleteme]", "").replace("[/deleteme]'", "")
    with open(os.path.join(basefolder,dicfile), "w+") as filename:
        filename.write(data)

makedir(basefolder)
with open(os.path.join(basefolder, "TODO"), "w+", encoding='utf-8') as todofile:
    pass
tasks = {"Abilities" : { "dictionary" : BattleAbilities, "file" : "abilities.py", "dicname" : "BattleAbilities"} , 
         "Moves": {"dictionary" : BattleMovedex, "file" : "moves.py", "dicname" : "BattleMovedex"} 
         }

for task in tasks:
    tododata = ""
    modulelist = []
    workingfolder = os.path.join(basefolder, task)
    dicdata = tasks[task]
    makedir(workingfolder)
    dicscan(dicdata["dictionary"])
    with open(os.path.join(basefolder, "TODO"), "a+", encoding='utf-8') as todofile:
        todofile.write("\n" + task + ":\n")
        todofile.write(tododata)
    writenewdict(dicdata["dictionary"], dicdata["dicname"], dicdata["file"])
    writenewinit()
    fixdict(dicdata["file"])

