from Character_Creation import Character
# this is used to break down the character even more so they become more individualized
#hp is amount of health
#str is amount of strength
#agi is amount of agility
#mana is used for skills
#aura unique attribute for archer and knight that empowers them
#intelligence is uinque attribute for mage that lets them have more skills and allows them to attack faster
# and deal more damage to enemies and monsters
#stealth is similar to intelligence for mages, but stealth doesn't give more skills but causes more damage if
# they have the first strike

class Knight(Character):
    def __init__(self, hp, str, agi, mana, aura):
        self.hp = hp
        self.str = str
        self.agi = agi
        self.mana = mana
        self.aura = aura

class Archer(Character):
    def __init__(self, hp, str, agi, mana, aura):
        self.hp = hp
        self.str = str
        self.agi = agi
        self.mana = mana
        self.aura = aura

class Mage(Character):
    def __init__(self, hp, str, agi, mana, intelligence):
        self.hp = hp
        self.str = str
        self.agi = agi
        self.mana = mana
        self.intelligence = intelligence

class Assassin(Character):
    def __init__(self, hp, str, agi, mana, stealth):
        self.hp = hp
        self.str = str
        self.agi = agi
        self.mana = mana
        self.stealth = stealth

