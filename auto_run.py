from heap import*
from logic import*
from random import randint
from itertools import permutations
P=80#average length of a path
def auto(fix,PT,EVENT,mobility,shuffle,E,C,L,G,INITIAL):
    m,n=len(fix),PT-sum(fix)
    X=heap(m,n)
    test=[list(array(fix)+array(_)) for _ in X]
    for deposit in test:
        max_P,counter=0,0
        print '================================'
        if shuffle:
            if sum(mobility)==0:all_kind=[[randint(300,700) for _ in range(PT)] for __ in range(200)]
            else:all_kind=set(list(permutations(mobility)))
        else:all_kind=[mobility]
        for team_speed in all_kind:
            passing,total=0,0
            if shuffle:counter+=1
            for __ in range(1000):#run times
                team=[]
                for i,times in enumerate(deposit):
                    for _ in range(times):team.append([INITIAL[i],EVENT[INITIAL[i]][0]])
                LOCKER=L
                ENEMY=[1 for _ in range(E)]
                CHANGER=[0 for _ in range(C)]
                GATE=[[False,[]] for _ in range(G)]
                PASS=[True for _ in range(PT)]
                speed_change=[{'tornado':[False,False],'spiderweb':[False,False]} for _ in range(PT)]
                ending=False
                while not ending:
                    for i in range(PT):
                        if PASS[i]:move(team[i],team_speed[i],speed_change[i])
                        while team[i][1]<=0 and not ending:
                            trial=team[i][0]
                            number=alphabet[trial[1]]
                            TYPE=trial[0]
                            if TYPE=='S':selector(trial,team[i],EVENT,len(EVENT[trial][1]))
                            elif TYPE=='E':enemy(trial,team[i],EVENT,ENEMY,number)
                            elif TYPE=='C':changer(trial,team[i],EVENT,CHANGER,number,len(EVENT[trial][1]))
                            elif TYPE=='T':teleport(trial,team[i],EVENT)
                            elif TYPE=='L':locker(trial,team[i],EVENT,LOCKER,number)
                            elif TYPE=='B':button(trial,team[i],EVENT,PASS,GATE,alphabet[EVENT[trial][1][1][1]])
                            elif TYPE=='G':gate(trial,team[i],EVENT,PASS,GATE,number,i)
                            elif TYPE=='A' or TYPE=='D':speed(trial,team[i],EVENT,speed_change[i],TYPE)
                            else:ending=True
                        if ending or not any(PASS):break
                if sum(ENEMY)==0:passing+=1.
                total+=1.
            if passing/total*100.>max_P:
                counter=0
                max_P=passing/total*100.
                print 'MAX!!!:',deposit,team_speed,max_P,'%'
            Prob=passing/total*100.
            if Prob==0. or Prob==100.:break
            if counter>40:#if u can't get a higher Prob for * times,change a new set
                print 'shimakaze:o soi~'
                break
