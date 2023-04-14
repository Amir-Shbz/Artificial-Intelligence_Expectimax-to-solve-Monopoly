class Agent():
    def __init__(self,name,Id):
        self.id = Id
        self.name = name
        self.money = 4000
        self.position = 0
         
    def ExpectiMax(self, curr_state, depth, IsMaxPlayer):
        action = 0
        if depth==0:
            return action, curr_state.evaluation()
        
        if IsMaxPlayer:
            max_value = float('-inf')
            for successor in curr_state.next_states(True, curr_state):
                action1, value = self.ExpectiMax(successor, depth-1, False)
                if value > max_value:
                    action=action1
                    max_value=value 
            return action, max_value
       
        else:
            ExpectedValue = 0
            for successor in curr_state.next_states(False, curr_state):
                action, value = self.ExpectiMax(successor, depth-1, True)
                ExpectedValue += (value*(1/6))
                
            return action, ExpectedValue 
        