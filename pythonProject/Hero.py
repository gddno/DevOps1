from pydoc import describe


class Hero():
    """Class to creat Hero for our Game"""

    def __init__(self, name, level, race):
        """Initiate our Hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """Print all aprametrs of this Hero"""
        discription = (self.name + " " + "Level is: " + str(self.level) + " Race is: " + self.race + " Health is: " + str(self.health)).title()
        print(discription)

    def level_up(self):
        """Upgrade Level of Hero"""
        self.level += 1
    
    def move(self):
        """Start moving Hero"""
        print("Hero " + self.name + " start moving...")

    def harm(self):
        """Harm to my Hero"""
        self.health -= 1

    def set_health(self, new_health):
        self.health = new_health