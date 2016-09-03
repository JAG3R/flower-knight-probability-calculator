from auto_run import*
fix=[?]#the least team arangement to avoid 0% pass
Enemy=?#number of enemies
Changer=?#number of changers
Locker=[?]#the numbers on each lockers
Gate=?#number of gates
INITIAL=[?]#initial targets for each camps
'''If you want to simulate more precisely, go to wiki and download the map or take screenshot.(MUST 960X640 pixels!!!!!!)
Edit the map by Paint. Draw a line between circles and you can see the line holds ?x? pixels.
Input the 2 arguments into the function--abc(,) and you can get the length of it.'''
##==================================================##
'''First, you need to mark all the selectors, enemies, changers, teleports, lockers, buttons, gates, tornados, spiderwebs with a,b,c...,z'''
EVENT ={'Sa':[?,['?','?']],#selector
        'Sb-1':[?,['?','?']],
        'Sb-2':[?,['?','?']],
        'Ea':[?,['?']],#enemy
        'Ca':[?,['?','?']],#changer
        'Ta':[?,['?']],#teleport
        'La':[?,['?','lock target']],#locker
        'Ba':[?,['?','belonging gate']],#button
        'Ga':[?,['?']],#gate
        'Aa':[?,['?']],#accel(tornado)
        'Da':[?,['?']],#decel(spiderweb)
        'end-1':[?],#end
        'end-2':[?]
        }
'''Each organ has two parts--[part1,[part2]]
for part1:
    simple version: replace ? with P*count (where count is the number of paths between circles) #P is average path length. I have set it
    precise version: replace ? with abc(*,*)+abc(*,*)+...+abc(*,*) (where * you need to measure it by Paint)
for part2:
    selector:

    enemy:
    changer:
    teleport:
    locker:
    button:
    gate:
    accel(tornado):
    decel(spiderweb):
    end has no part2.
'''
##==================================================##
#input your 5 teams mobility. u can also input 4 or 3 teams.(rare to use)
#if u want to find best mobility:team_speed=[0,0,0,0,0]
team_speed=[?,?,?,?,?]
#shuffle=True:shuffle your team_speed order to get a little higher probability(may spend a little bit longer time)
shuffle=False

if sum(team_speed)==0:shuffle=True
auto(fix,len(team_speed),EVENT,team_speed,shuffle,Enemy,Changer,Locker,Gate,INITIAL)

