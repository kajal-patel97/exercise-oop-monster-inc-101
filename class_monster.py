class Monster():


    # Monster attributes
    def __init__(self, name, skills = ['Scary']):
        self.name = name
        self.skills = skills

    #Monster Methods

    def sleep(self):
        return 'ZZZZzzzzZZZzz'
    def eat(self):
        return 'NOM NOM NOM'
    def scare_attack(self):
        return 'RAAAAHHHHH!!!... RAWWRRRRRR!!!!'
