from  class_monster import *

monster1 = Monster('Paul', ['scary', 'hairy', 'loud'])
monster2 = Monster('David')

print(monster1.name)
print(monster2.skills)

monster2.added_skills('heals quick', 'shy')
print(monster2.skills)