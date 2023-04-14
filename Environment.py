from numpy.random import randint

Go = ["Go",0,0,-1]
MediterRanean_Avenue = ["Mediter Ranean Avenue",25,5,0]
Chest1 = ["Chest I",50,0,0]
Baltic_Avenue = ["Baltic Avenue",35,10,0]
Income_Tax = ["Income Tax",100,0,0]
Reading_Railroad = ["Reading Railroad",100,25,0]
Oriental_Avenue = ["Oriental Avenue",50,15,0]
Chance1 = ["Chance I",100,0,0]
Vermont_Avenue = ["Vermont Avenue",55,17,0]
Connecticut_Avenue = ["Connecticut Avenue",60,20,0]
Just_Visiting_In_Jail = ["Just Visiting In Jail",0,0,2]
StCharles_Place = ["St.Charles Place",75,30,0]
Electric_Company = ["Electric_Company",250,90,0]
States_Avenue = ["States Avenue",80,32,0]
Virginia_Avenue = ["Virginia Avenue",85,35,0]
Pensylvania_Railroad = ["Pensylvania_Railroad",250,90,0]
StJames_Place = ["St.James Place",100,40,0]
Chest2 = ["Chest II",50,0,0]
Tennessee_Avenue = ["Tennessee Avenue",150,50,0]
NewYork_Avenue = ["NewYork Avenue",175,55,0]
Free_Parking = ["Free Parking",0,0,0]
Kentucky_Avenue = ["Kentucky_Avenue",200,70,0]
Chance2 = ["Chance II",100,0,0]
Indiana_Avenue = ["Indiana Avenue",250,90,0]
Illinois_Avenue = ["Illinois Avenue",300,100,0]
B_and_O_Railroad = ["B & O Railroad",500,125,0]
Atlantic_Avenue = ["Atlantic Avenue",400,110,0]
Ventnor_Avenue = ["Ventnor Avenue",450,115,0]
Water_Works = ["Water Works",750,125,0]
Marvin_Gardens = ["Marvin Gardens",500,120,0]
Go_to_Jail = ["Go to Jail",0,0,2]
Pacific_Avenue = ["Pacific Avenue",750,125,0]
North_Carolina_Avenue = ["North Carolina Avenue",800,130,0]
Chest3 = ["Chest III",50,0,0]
Pensylvania_Avenue = ["Pensylvania Avenue",850,135,0]
Short_Line = ["Short Line",750,125,0]
Chance3 = ["Chance III",100,0,0]
Park_Place = ["Park Place",1000,150,0]
Luxury_Tax = ["Luxury Tax",250,0,0]
Board_Walk = ["Board_Walk",1250,175,0]

Places=[Go,
        MediterRanean_Avenue,
        Chest1,
        Baltic_Avenue,
        Income_Tax,
        Reading_Railroad,
        Oriental_Avenue,
        Chance1,
        Vermont_Avenue,
        Connecticut_Avenue,
        Just_Visiting_In_Jail,
        StCharles_Place,
        Electric_Company,
        States_Avenue,
        Virginia_Avenue,
        Pensylvania_Railroad,
        StJames_Place,
        Chest2,
        Tennessee_Avenue,
        NewYork_Avenue,
        Free_Parking,
        Kentucky_Avenue,
        Chance2,
        Indiana_Avenue,
        Illinois_Avenue,
        B_and_O_Railroad,
        Atlantic_Avenue,
        Ventnor_Avenue,
        Water_Works,
        Marvin_Gardens,
        Go_to_Jail,
        Pacific_Avenue,
        North_Carolina_Avenue,
        Chest3,
        Pensylvania_Avenue,
        Short_Line,
        Chance3,
        Park_Place,
        Luxury_Tax,
        Board_Walk]

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

class Environment:
    def __init__(self, begin_state, agents:list, actions):
        self.map = Places
        self.curr_state = begin_state
        self.agents = agents
        self.winner = -2
        self.action = actions

    def step(self, agent, depth):
        if agent.id == -1:
            position = randint(1,6)
            self.agents[0].position += position
            x = int(input())
            y = self.action[x]()
            new_state = y.apply(self.curr_state, agent.position)

        elif agent.id == 1:
            action, value = agent.ExpectiMax(self.curr_state, depth, True)
            y = self.action[action]()
            new_state = y.apply(self.curr_state, agent.position)
            self.curr_state = new_state
            if self.curr_state.isTerminal:
                self.winner = agent.id
                return True
            return False
        