# from random import randint
# from State import env


#     def roll(self):
#         self.dice1=randint(1,6)
#         self.dice2=randint(1,6)
#         x = self.dice1 + self.dice2
#         self.position = (self.position + x)%40   

class Agent():
    def __init__(self,name):
        self.name = name
        self.money = 4000
        self.position = 0
        self.number = 1 # Default is Max player.

    def play(self, curr_state):
        action = -1
        
        


    def expected_value(self):
        pass

    def max_value(self):
        pass    