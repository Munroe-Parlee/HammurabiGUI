import math
import random
class GameModel:

    def __init__(self):
        #config
        self.bushels_per_person = 20
        self.acres_planted_per_bushel = 2
        self.acres_farmed_per_person = 10

        #stats
        self.year = 1
        self.bushels = 3500
        self.population = 100
        self.acres = 1000
        self.acres_planted = 0
        self.acres_price = 20
        pass

    def get_bushels_per_person(self):
        return self.bushels_per_person

    def get_acres_planted_per_bushel(self):
        return self.acres_planted_per_bushel

    def get_acres_farmed_per_person(self):
        return self.acres_farmed_per_person

    def get_year(self):
        return self.year

    def get_bushels(self):
        return self.bushels

    def get_population(self):
        return self.population

    def get_acres(self):
        return self.acres

    def get_acres_planted(self):
        return self.acres_planted

    def get_acres_price(self):
        return self.acres_price
    
    def __str__(self):
        return f"Year {self.get_year()}\nBushels: {self.get_bushels()}\nPopulation: {self.get_population()} people\nAcres: {self.get_acres()}\nPrice per acre: {self.get_acres_price()} bushels"


    def enter_input(self, buy, sell, plant, feed):
        if ((feed + plant + (sell - buy)*self.acres_price) > self.bushels or (plant*self.acres_planted_per_bushel > self.acres + (buy - sell)) or (plant*self.acres_planted_per_bushel > self.acres_farmed_per_person * self.get_population())):
             raise Exception
        else:
            self.land_purchase(buy, sell)
            self.harvest(plant)
            self.starve(feed)
            self.acres_price_swing()
            self.year = self.year +1
        pass

    def land_purchase(self, buy, sell):
        self.bushels = self.bushels + (sell - buy)*self.acres_price
        self.acres = self.acres + buy - sell
        pass
    
    def harvest(self, plant):
        self.bushels = self.bushels - plant
        self.acres_planted = plant*self.acres_planted_per_bushel
        self.bushels = self.bushels + (self.acres_planted)*random.randint(1, 5)
        self.acres_planted = 0
        pass

    def starve(self, feed):
        if self.get_population() * self.get_bushels_per_person() > feed:
            self.population = (feed - feed % 20)/self.get_bushels_per_person()
        pass

    def acres_price_swing(self):
        self.acres_price = 16 + random.randint(0, 8)
        pass