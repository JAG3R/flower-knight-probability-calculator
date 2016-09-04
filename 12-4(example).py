from data import P
from auto_run import*
fix=[1,0,1,1]#the least team arangement to avoid 0% pass
Enemy=8#number of enemies
Changer=0#number of changers
Locker=[]#the numbers on each lockers
Gate=0#number of gates
INITIAL=['Ea','Sb-1','Eb','Ec']#initial targets for each camps
'''If you want to simulate more precisely, go to wiki and download the map or take screenshot.(MUST 960X640 pixels!!!!!!)
Edit the map by Paint. Draw a line between circles and you can see the line holds ?x? pixels.
Input the 2 arguments into the function--abc(,) and you can get the length of it.'''
##==================================================##
'''First, you need to mark all the targets with a,b,c...,z
There may be more than 1 path that come into the target.
In this case, append -1,-2 after the target to enumerate it.'''
EVENT ={'Sa-1':[P*4,['Ef','Sd-1']],#selector
        'Sa-2':[P*3,['Ef','Sd-1']],
        'Sb-1':[P*4,['Sa-2','Sc-1']],
        'Sb-2':[P*3,['Sa-2','Sc-1']],
        'Sc-1':[P*2,['Sd-2','Ee-1']],
        'Sc-2':[P*2,['Sd-2','Ee-1']],
        'Sd-1':[P*3,['Eh-2','Eg']],
        'Sd-2':[P*3,['Eh-2','Eg']],
        'Se':[P*1,['Ed','Ee-2','Eh-5']],
        'Ea':[P*2,['Sa-1']],#enemy
        'Eb':[P*1,['Sb-2']],
        'Ec':[P*1,['Se']],
        'Ed':[P*1,['Sc-2']],
        'Ee-1':[P*1,['Eh-4']],
        'Ee-2':[P*2,['Eh-4']],
        'Ef':[P*2,['Eh-1']],
        'Eg':[P*1,['Eh-3']],
        'Eh-1':[P*4,['end']],
        'Eh-2':[P*4,['end']],
        'Eh-3':[P*3,['end']],
        'Eh-4':[P*5,['end']],
        'Eh-5':[P*6,['end']],
        'end':[P*2]
        }
'''Each target has two PARTs--[PART1,[PART2]]
for PART1:
    PART1 stands for the distance to reach the target.
    simple version: replace ? with P*count (where count is the number of paths between targets) #P is the average path length. I have set it
    precise version: replace ? with abc(*,*)+abc(*,*)+...+abc(*,*) (where * you need to measure it by Paint)
for PART2:
    PART2 stands for the next target(s) which you might touch.
    selector: List all the next targets that this selector would go to.
    enemy: The next target(1)
    changer: List all the next targets that this changer would go to.
    teleport: The next target(1)
    locker: The next target(1),lock target(1)
    button: The next target(1),belonging gate(1)
    gate: The next target(1)
    accel(tornado): The next target(1)
    decel(spiderweb): The next target(1)
    end has no PART2.
'''
##==================================================##
'''Input your 5 teams mobility. You can also input 4 or 3 teams.(rare to use)'''
##If you want to find best mobility:team_speed=[0,0,0,0,0]
team_speed=[727,727,727,727,727]
##shuffle=True:shuffle your mobility order to get a bit higher probability(may spend a little bit longer time)
shuffle=False

if sum(team_speed)==0:shuffle=True
auto(fix,len(team_speed),EVENT,team_speed,shuffle,Enemy,Changer,Locker,Gate,INITIAL)
