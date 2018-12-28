class BattleData:

    def __init__(self):
        # These will eventually be classes
        self.teams = {"A": Teams(), "B": Teams()}
        self.battle = Battle()
        self.turndata = TurnData()


class Teams:
    pass


class Battle:
    pass


class TurnData:
    pass


class Pokemon:
    pass

