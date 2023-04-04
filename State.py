from random import randint

class State():
    def __init__(self,curr_player_number:int = -1):
        self.isTerminal = False
        self.value = self.calculate_value()
        self.curr_player_number = curr_player_number

    def calculate_value(self):
        value = 0
        
        pass

    def check_potential(self, start, end):
        
        pass

    def apply_action(self):

        pass

    def next_states(self):
        for action in range(len(self.board[0])):
            new_state = self.apply_action(action, self.curr_player_number)
            if new_state != None:
                yield (action, new_state)
        