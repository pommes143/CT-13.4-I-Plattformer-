#! /usr/bin/python3

class Spieler(object):
    """docstring for Spieler."""
    health = 0
    stamina = 0
    strengh = 0
    agility = 0
    luck = 0
    charisma = 0
    mana = 0

    def __init__(self, arg):
        super(Spieler, self).__init__()
        self.arg = arg
