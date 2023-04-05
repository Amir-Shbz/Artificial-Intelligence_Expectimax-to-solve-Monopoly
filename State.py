class State():

    def __init__(self,agent):
        self.isTerminal = self.isTerminal()
        self.value = self.calculate_value()
        self.agent = agent

    def isTerminal(self):
        if self.agent.position == 0:
            return True
        return False          

    def evaluation(self):
        gamma = -2
        value = (self.agent.money)+(gamma*(39-self.agent.position))
        return value

    def next_states(self):
        for action in range(len(self.board[0])):
            new_state = self.apply_action(action, self.curr_player_number)
            if new_state != None:
                yield (action, new_state)   

    def apply_action(self):

        pass
                 