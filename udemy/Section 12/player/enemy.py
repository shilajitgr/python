class Enemy:
# the above line is equivalent to "class Enemy(object)"
    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.lives = lives
        self.hit_points = hit_points
        self.alive = True
        
    def takeDamage(self,damage):
        remaining_points = self.hit_points - damage
        if remaining_points > 0:
            self.hit_points = remaining_points
            print(f'{self.name} took {damage} points of damage and has {self.hit_points} left')
        else:
            self.lives -= 1
            if self.lives > 0:
                print(f'{self.name} lost a life')
            else:
                print(f'{self.name} is dead')
                self.alive = False
                
    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Hit Points: {0.hit_points}".format(self)  

    # def hit(self):
    #     self.lives -= 1
    #     if self.lives <= 0:
    #         print(f'{self.name} has died')
    #     else:
    #         print(f'{self.name} has {self.lives} lives left')
    
    
class Troll(Enemy):
    
    def __init__(self, name, hit_points=0, lives=1):   
        # this init method overwrites the parent's
        # hence, any initialization of Troll class that does not match the
        # signature of the init(), will throw an error
        
        Enemy.__init__(self,name, hit_points, lives)
        """ 
        super(Troll, self).__init__(name)
        super().__init__(name)    # same as above line
        """
        
    def grunt(self):
        print("Me {0.name}. {0.name} stomp you!".format(self))
        

class Vampyre(Enemy):
    
    def __init__(self, name, hit_points=12, lives=1):
       super().__init__(name, hit_points, lives) 