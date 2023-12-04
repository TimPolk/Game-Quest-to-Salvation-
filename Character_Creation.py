from Jobs import Knight
from Jobs import Archer
from Jobs import Mage
from Jobs import Assassin
class Character:
    def __int__(self, Job, Level, Weapon, Skills):
        self.Job = Job
        self.Level = Level
        self.Weapon = Weapon
        self.Skills = Skills

    def character_job(self):
        if self.Job == "Knight":
            self.job = Knight

        if self.Job == "Archer":
            self.job = Archer

        if self.Job == "Mage":
            self.job = Mage

        if self.Job == "Assassin":
            self.job = Assassin

    def level_up(self, Level, exp):
        if Level == 1:
            if exp == 5:
                Level = 2
        elif Level == 2:
            if exp == 10:
                Level = 3
        elif Level == 3:
            if exp == 15:
                Level = 3
        elif Level == 4:
            if exp == 20:
                Level = 5
        elif Level == 5:
            if exp == 25:
                Level = 6
        elif Level == 6:
            if exp == 30:
                Level = 7
        elif Level == 7:
            if exp == 35:
                Level = 8
        elif Level == 8:
            if exp == 40:
                Level = 9
        elif Level == 9:
            if exp == 45:
                Level = 10
    
    
        
        
