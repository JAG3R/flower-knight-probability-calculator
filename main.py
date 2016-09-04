from auto_run import*
fix=[?]#the least team arangement to avoid 0% pass
Enemy=?#number of enemies
Changer=?#number of changers
Locker=[?]#the numbers on each lockers (If no lockers, just remove the '?')
Gate=?#number of gates
INITIAL=[?]#initial targets for each camps
'''If you want to simulate more precisely, go to wiki and download the map or take screenshot.(MUST 960X640 pixels!!!!!!)
Edit the map by Paint. Draw a line between circles and you can see the line holds ?x? pixels.
Input the 2 arguments into the function--abc(,) and you can get the length of it.'''
##==================================================##
'''First, you need to mark all the targets with a,b,c...,z
There may be more than 1 path that come into the target.
In this case, append -1,-2 after the target to enumerate it.'''
EVENT ={'Sa':[?,['?','?']],#selector
        'Sb-1':[?,['?','?']],
        'Sb-2':[?,['?','?']],
        'Ea':[?,['?']],#enemy
        'Ca':[?,['?','?']],#changer
        'Ta':[?,['?']],#teleport
        'La':[?,['?','?']],#locker
        'Ba':[?,['?','?']],#button
        'Ga':[?,['?']],#gate
        'Aa':[?,['?']],#accel(tornado)
        'Da':[?,['?']],#decel(spiderweb)
        'end-1':[?],#end
        'end-2':[?]
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
team_speed=[?,?,?,?,?]
##shuffle=True:shuffle your mobility order to get a bit higher probability(may spend a little bit longer time)
shuffle=False
##==================================================##




if sum(team_speed)==0:shuffle=True
auto(fix,len(team_speed),EVENT,team_speed,shuffle,Enemy,Changer,Locker,Gate,INITIAL)

