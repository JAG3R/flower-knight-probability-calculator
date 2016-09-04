from auto_run import*
fix=input("fix(least arangement):")#the least team arangement to avoid 0% pass
Enemy=input("Enemy(number of pests):")#number of enemies
Changer=input("Changer(number of blue converters):")#number of changers
Locker=input("Locker(the numbers on each lockers):")#the numbers on each lockers (If no lockers, just remove the '?')
Gate=input("Gate(number of gates):")#number of gates
INITIAL=input("INITIAL(initial targets):")#initial targets for each camps
EVENT =input("EVENT(datas of all targets):")
team_speed=input("team mobilities(find best mobility input [0,0,0,0,0]):")
y,n=1,0
shuffle=input("shuffle the team order(y/n):")
if sum(team_speed)==0:shuffle=True
else:
    if y:shuffle=True
    else:shuffle=False
auto(fix,len(team_speed),EVENT,team_speed,shuffle,Enemy,Changer,Locker,Gate,INITIAL)


