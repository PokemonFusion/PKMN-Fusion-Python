def addlog(dictionary: dict, log: str):
    if 'log' not in dictionary:
        dictionary['log'] = list()

    dictionary['log'].append(log)