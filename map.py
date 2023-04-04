from random import randint

MediterRanean_Avenue = ["Mediter Ranean Avenue",25,5]
Chest1 = ["Chest I",50,0]
Baltic_Avenue = ["Baltic Avenue",35,10]
Income_Tax = ["Income Tax",100,0]
Reading_Railroad = ["Reading Railroad",100,25]
Oriental_Avenue = ["Oriental Avenue",50,15]
Chance1 = ["Chance I",100,0]
Vermont_Avenue = ["Vermont Avenue",55,17]
Connecticut_Avenue = ["Connecticut Avenue",60,20]
Just_Visiting_In_Jail = ["Just Visiting In Jail",0,0]
StCharles_Place = ["St.Charles Place",75,30]
Electric_Company = ["Electric_Company",250,90]
States_Avenue = ["States Avenue",80,32]
Virginia_Avenue = ["Virginia Avenue",85,35]
Pensylvania_Railroad = ["Pensylvania_Railroad",250,90]
StJames_Place = ["St.James Place",100,40]
Chest2 = ["Chest II",50,0]
Tennessee_Avenue = ["Tennessee Avenue",150,50]
NewYork_Avenue = ["NewYork Avenue",175,55]
Free_Parking = ["Free Parking",0,0]
Kentucky_Avenue = ["Kentucky_Avenue",200,70]
Chance2 = ["Chance II",100,0]
Indiana_Avenue = ["Indiana Avenue",250,90]
Illinois_Avenue = ["Illinois Avenue",300,100]
B_and_O_Railroad = ["B & O Railroad",500,125]
Atlantic_Avenue = ["Atlantic Avenue",400,110]
Ventnor_Avenue = ["Ventnor Avenue",450,115]
Water_Works = ["Water Works",750,125]
Marvin_Gardens = ["Marvin Gardens",500,120]
Go_to_Jail = ["Go to Jail",0,0]
Pacific_Avenue = ["Pacific Avenue",750,125]
North_Carolina_Avenue = ["North Carolina Avenue",800,130]
Chest3 = ["Chest III",50,0]
Pensylvania_Avenue = ["Pensylvania Avenue",850,135]
Short_Line = ["Short Line",750,125]
Chance3 = ["Chance III",100,0]
Park_Place = ["Park Place",1000,150]
Luxury_Tax = ["Luxury Tax",250,0]
Board_Walk = ["Board_Walk",1250,175]

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

players = []

class Game:
    self.Players = players

    def check_bankrupt():
        for x in self.Players:
            if x.money < 0:
                print(x.name, " has bankrupted he/she can't play anymore")

    def check_winner():
        for x in self.Players:
            if x.position = 0:
                print(f"{x.name} won!")
                break
                            
