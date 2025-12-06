import math
import random
class GameModel:

    def __init__(self):
        self.bushels = 3500
        self.population = 100
        self.acres = 1000
        self.acres_planted = 0
        self.acres_price = 20
        pass
    
    def harvest(self):
        self.bushels = self.bushels + (self.acres_planted)*random.randint(1, 5)
        self.acres_planted = 0
        pass
    
    def acres_price_swing(self):
        self.acres_price = 16 + random.randint(0, 8)
        pass