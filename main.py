from auto_run import*
fix=[?]#the necessary team to avoid 0% pass
Enemy=?#enemy numbers
Changer=?#changer numbers
Locker=[?]#the numbers on each lockers
Gate=?#gate numbers
INITIAL=[?]#initial targets for each camps
'''if u want to simulate more precisely, go to wiki and download the map.
Edit the map by Paint. Draw a line between circles and you can see the line holds ?x? pixels.
Input the 2 arguments into the function--abc(,) and you can get the length of it.'''
##P*? can be replaced by abc(*,*)+...+abc(*,*)
EVENT ={'Sa':[P*?,['?','?']],#selector
        'Ea':[P*?,['?']],#enemy
        'Ca':[P*?,['?','?']],#changer
        'Ta':[P*?,['?']],#teleport
        'La':[P*?,['0','1']],#locker #0:next, 1:lock target
        'Ba':[P*?,['0','1']],#button #0:next, 1:belonging gate(e.g.'Ga')
        'Ga':[P*?,['?']],#gate
        'Aa':[P*?,['?']],#accel:tornado
        'Da':[P*?,['?']],#decel:spiderweb
        'end':[P*?]#end
        }
#input your 5 teams mobility. u can also input 4 or 3 teams.(rare to use)
#if u want to find best mobility:team_speed=[0,0,0,0,0]
team_speed=[?,?,?,?,?]
#shuffle=True:shuffle your team_speed order to get a little higher probability(may spend a little bit longer time)
shuffle=False

if sum(team_speed)==0:shuffle=True
auto(fix,len(team_speed),EVENT,team_speed,shuffle,Enemy,Changer,Locker,Gate,INITIAL)

