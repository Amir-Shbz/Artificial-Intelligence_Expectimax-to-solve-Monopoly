class Agent():
    def __init__(self,name):
        self.id = 0
        self.name = name
        self.money = 4000
        self.position = 0
         
    def ExpectiMax(self, curr_state, depth, IsMaxPlayer):
        action = 0
        if depth==0:
            return action, curr_state.evaluation()
        
        if IsMaxPlayer:
            max_value = float('-inf')
            for successor in curr_state.next_states():
                action1, value = self.ExpectiMax(successor, depth-1, False)
                if value > max_value:
                    action=action1
                    max_value=value 
            return action, max_value
       
        else:
            ExpectedValue = 0
            for successor in curr_state.next_states():
                action, value = self.ExpectiMax(successor, depth-1, True)
                ExpectedValue += (value*(1/6))
                
            return action, ExpectedValue 
        