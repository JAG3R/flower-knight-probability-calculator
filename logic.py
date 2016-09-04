from data import*
from random import*
alphabet={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
def move(team,team_speed,speed):#running
    if speed['tornado'][0]:
        team[1]-=ac*px_unit(team_speed)
        speed['tornado'][0]=False
    elif speed['spiderweb'][0]:
        team[1]-=de*px_unit(team_speed)
        speed['spiderweb'][0]=False
    else:
        team[1]-=px_unit(team_speed)
        speed['tornado'][1],speed['spiderweb'][1]=False,False

def trans(trial,team,EVENT,Z):#Z:No. of next target
    NEXT=EVENT[trial][1][Z]
    team[0]=NEXT
    team[1]+=EVENT[NEXT][0]
    return team

def selector(trial,team,EVENT,n):
    choice=randint(0,n-1)
    team=trans(trial,team,EVENT,choice)

def enemy(trial,team,EVENT,ENEMY,E):
    ENEMY[E]=0
    team=trans(trial,team,EVENT,0)

def changer(trial,team,EVENT,CHANGER,C,n):
    if CHANGER[C]<n:
        team=trans(trial,team,EVENT,CHANGER[C])
        CHANGER[C]+=1
    else:
        CHANGER[C]=0
        team=trans(trial,team,EVENT,CHANGER[C])

def teleport(trial,team,EVENT):
    team[1]=0
    team=trans(trial,team,EVENT,0)

def locker(trial,team,EVENT,LOCKER,L):
    if LOCKER[L]>0:team=trans(trial,team,EVENT,0)
    else:team=trans(trial,team,EVENT,1)
    LOCKER[L]-=1

def button(trial,team,EVENT,PASS,GATE,G):
    if GATE[G][0]:pass
    else:
        GATE[G][0]=True
        for i in set(GATE[G][1]):PASS[i]=True
    team=trans(trial,team,EVENT,0)

def gate(trial,team,EVENT,PASS,GATE,G,i):
    if GATE[G][0]:team=trans(trial,team,EVENT,0)
    else:
        team[0],team[1]=trial,0.01
        PASS[i]=False
        GATE[G][1].append(i)

def speed(trial,team,EVENT,speed,AD):
    if AD=='A':type_AD,c=speed['tornado'],ac
    if AD=='D':type_AD,c=speed['spiderweb'],de
    a=random()
    if a<ts_prob:
        if speed['tornado'][1]:rest=float(team[1]/ac)
        elif speed['spiderweb'][1]:rest=float(team[1]/de)
        else:rest=float(team[1])
        team[1]=float(rest*c)
        type_AD[0],type_AD[1]=True,True
    team=trans(trial,team,EVENT,0)
