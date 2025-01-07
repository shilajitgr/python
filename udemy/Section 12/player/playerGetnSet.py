class Player:
    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0
    
    def _lives_get(self):   # protected method
        return self._lives
    
    def _lives_set(self, lives):    #protected method
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0
    
    def _level_get(self):
        return self._level

    def _level_set(self, level):
        if level >= 0:
            delta = level - self._level
            self.score += delta * 1000
            self._level = level
        else:
            print("Level cannot be less than 1")
            # self._level = 1
    
    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score
    
    lives = property(fget=_lives_get, fset=_lives_set)  
    level = property(fget=_level_get, fset=_level_set)
    # property is a built-in function in python
    # now everytime lives is being referenced with class object, 
    # it will call _lives_get() method when fetching the value
    # and _lives_set() method when updating the value.