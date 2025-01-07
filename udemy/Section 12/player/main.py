from playerGetnSet import Player

tim = Player("Tim")

tim.level = 2
print(tim)

tim.level += 5  # this adds 5 to the existing value of tim.level and passes that to the setter

print(tim)

tim.poor = 500  
# even though this attr is not defined in the class, 
#it is being set when a value is assigned to it
print(tim.poor)

tim.score = 500
print(tim)

from enemy import Enemy
random_monster = Enemy("Basic enemy", 12, 1)
print(random_monster)
random_monster.takeDamage(4)
print(random_monster)

random_monster.takeDamage(9)
print(random_monster)

"""
Now, if you change the accessibility of lives data member to public, and run this code, it crash.
This is the result of self call by _lives_set() because now, lives data member being set by 
the setter is using "self.lives" which is also the reference to the property "self.lives"
whenever tim.lives is called, this results in an infinite recursion.
"""
