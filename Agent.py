from random import randint
from Map import env

class Agent:
    def __init__(self, name):
        self.name = name
        self.money = 4000
        self.position = 0

    def roll(self):
        self.dice1=randint(1,6)
        self.dice2=randint(1,6)
        x = self.dice1 + self.dice2
        self.position = (self.position + x)%40    
