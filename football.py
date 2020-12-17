import random
iD=0 #global id for each object
footballSociety=[] #global society of captains and players
class Person:
    id #local id declaration
    skill=0
    team=0 #team nubmer
    def __init__(self,t,s):
        global iD 
        global footballSociety
        self.team=t #team selection
        self.id=iD #this objects id
        iD+=1 #id change for next object
        self.skill=s #persons football playing skill
        #every time person is created, he is added to and can be found in footbalSociety
        footballSociety.append(self) 
        
        
    def getSkill(self): #we could use just h1.skill, but whatever, i cant explain why i added this
        return self.skill
    def getId(self): #the same as getSkill() func
        return self.id
    def getPerson(self): #and when i was writing this it just hits me. but this func just contains print line i need, so this is fine
        print("This persons skill level is ", self.getSkill()," and he played in team ", self.team)
        
class Captain(Person):
    spec="Captain"
    win=0 #each Captain starts with zero amount of wins
    def winUp(self):
        self.win=self.win+1 #win
    def getWins(self):
        return self.win
        
class footbalPlayer(Person):
    spec="player"
    def followCaptain(self,Captain): #footbalPlayer plays in a team of one of the captains
        print("footbalPlayer #", self.id, " follows Captain #", Captain.id)

h1=Captain(1, random.randint(7, 10)) #new Captains must have high playing skills
h2=Captain(2, random.randint(7, 10))

#now game begins
game=True
while game:
    team1=[] #team of captain 1 creation
    for i in range(10): #football team consists of 11 players, and the captain is one of them
        team1.append(footbalPlayer(1,random.randint(1, 10)))
    team2=[] #team of captain 2 creation
    for i in range(10):
        team2.append(footbalPlayer(2,random.randint(1, 10)))
    
    teamSkill_1=h1.getSkill() #counting team skill, captains skill is always the same after captain craation
    for i in range (len(team1)): #but each player skill is different in every game (different players)
        teamSkill_1+=team1[i].getSkill() #so we get each players skill and add it cumulatively to captains skill
    
    teamSkill_2=h2.getSkill()
    for i in range (len(team2)):
        teamSkill_2+=team2[i].getSkill()
    print(teamSkill_1," and ", teamSkill_2)
    #next fragment is skill comparison to define who won
    if teamSkill_1>teamSkill_2:
        h1.winUp()
        print("Captain 1 wins ", h1.getWins(), " times!")
    elif teamSkill_1<teamSkill_2:
        h2.winUp()
        print("Captain 2 wins ", h2.getWins(), " times!")
    else:
        print("Draw!") #this code makes draw quite rare
    
    if int(input("To continue enter 1, to exit enter any other number"))!=1: #just to stop the games
        game=False
        print("Championship statistics!\nTeam 1 with captains skill level ",h1.getSkill()," won ",h1.getWins()," times!") #championship results
        print("And team 2 with captains skill level ",h2.getSkill()," won ", h2.getWins(), " times!")
        #lets try to find a player and get his skill level and team
        #search starts after championship is ended, so we enter another loop for it
        search=True
        while search:
            ans=input("Enter players id to know his skill and team he played in")
            if ans=="exit": #to exit this loop
                search=False
            elif int(ans)<=iD: #iD is global and unique for each created person type
                for k in range(len(footballSociety)):
                    if footballSociety[k].getId()==int(ans):
                        if footballSociety[k].spec=="Captain":
                            print("This person is a Captain and he won ",footballSociety[k].getWins()," times!")
                        footballSociety[k].getPerson()
            else:
                print("There is no person with this ID!")
            
  
