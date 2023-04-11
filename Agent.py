class Agent():
    def __init__(self,name):
        self.name = name
        self.money = 4000
        self.position = 0
         
    def ExpectiMax(self, curr_state, depth, IsMaxPlayer):
        action = 0
        if depth==0:
            return action, curr_state.evaluation()
        
        if IsMaxPlayer:
            max_value = float('-inf')
            for successor in curr_state.next_states(IsMaxPlayer):
                action,value = ExpectiMax(successor, depth-1, False)
                if value > max_value:
                    bestmove=successor
                    max_value=value 
            return bestmove,max_value
       
        else:
            ExpectedValue = 0
            for successor in curr_state.get_successors():
                bestmove,value = ExpectiMax(successor, depth-1, True)
                ExpectedValue += value* successor.Probability()
                
            return bestmove,ExpectedValue 
        