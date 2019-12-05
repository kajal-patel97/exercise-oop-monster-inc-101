class Monster():

    # - Looks of a monster(Attributes)
    # - Should have a name that is a string
    # - Should have list of skills


    def __init__(self, name, skills = ['']):
        self.name = name
        self.skills = skills

    #Monster Methods

    def sleep(self):
        return 'ZZZZzzzzZZZzz'

    def eat(self):
        return 'NOM NOM NOM'
    def scare_attack(self):
        return 'RAAAAHHHHH!!!... RAWWRRRRRR!!!!'
