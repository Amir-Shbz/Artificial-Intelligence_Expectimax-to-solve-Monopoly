import Environment
import State
import Agent

class Buy:
    def apply(self, state, position):
        state.agent.money -= Places[position][1]
        Places.append(state.agent.id)

        return state

class Rent:
    def apply(self, state, agent2, position):
        state.agent.money -= Places[position][1]
        agent2.money += Places[position][2]

        return state
        
class Play_from_Go:
    def apply(self, state):
        state.agent.position = 0 

        return state

actions = [Buy, Rent, Play_from_Go]

agent = Agent('ash', -1)

begin_state = State(agent)
env = Environment(begin_state, [agent], actions)

while not env.step():
    pass