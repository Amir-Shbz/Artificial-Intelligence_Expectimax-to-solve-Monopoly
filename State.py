class State():

    def __init__(self, agent):
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
        pass              