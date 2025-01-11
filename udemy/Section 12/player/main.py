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

from enemy import Enemy, Troll, Vampyre

# random_monster = Enemy("Basic enemy", 12, 1)
# print(random_monster)
# random_monster.takeDamage(4)
# print(random_monster)

# random_monster.takeDamage(9)
# print(random_monster)
ugly_troll = Troll("Pug")
print("ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug", 18, 1)
print("Another troll - {}".format(another_troll))

brother = Troll("Urg", 23)
print(brother)

print(end="\n\n\n")
ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

print(end="\n\n\n")
ugly_troll.takeDamage(4)
print(ugly_troll)
bad_vamp = Vampyre("Evil")
bad_vamp.takeDamage(7)
print(bad_vamp)
while bad_vamp.alive:
    bad_vamp.takeDamage(1)
"""
Now, if you change the accessibility of lives data member to public, and run this code, it crash.
This is the result of self call by _lives_set() because now, lives data member being set by 
the setter is using "self.lives" which is also the reference to the property "self.lives"
whenever tim.lives is called, this results in an infinite recursion.
"""
