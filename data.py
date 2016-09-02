from numpy import*
'''If you want to get a more precise data,go to wiki and download the map.
Edit the JPG file with Paint. Draw a line between circles and you can see the line holds ?x? pixels.
Input the 2 arguments into the function--abc and you can get the length of it.'''
def abc(a,b):
    return sqrt(a**2+b**2)
speed=[656,478,583,416,419,406,611,661,486]
speed[0]=(abc(62,41)+abc(40,76)+abc(27,41))/speed[0]
speed[1]=(abc(114,1)+abc(26,25))/speed[1]
speed[2]=(abc(83,63)+abc(74,9))/speed[2]
speed[3]=(abc(62,41)+abc(22,45))/speed[3]
speed[4]=(abc(83,63)+abc(21,4))/speed[4]
speed[5]=(abc(79,42)+abc(9,40))/speed[5]
speed[6]=(abc(52,49)+abc(45,74)+abc(22,9))/speed[6]
speed[7]=(abc(81,43)+abc(30,112))/speed[7]
speed[8]=(abc(47,45)+abc(40,60))/speed[8]
##speed[9]=(abc()+abc())/speed[9]
##speed[10]=(abc()+abc())/speed[10]

##print sum(speed)/len(speed)

def px_unit(x):
    return x*0.305976092846

A,B=[],[]
A.append( (abc(36,40)+abc(89,18)+abc(109,8)+abc(20,2)) / (abc(52,49)+abc(45,74)+abc(22,9)) )
B.append( (abc(45,1)) / (abc(81,43)+abc(30,112)) )
A.append( (abc(76,79)+abc(95,17)+abc(36,3)) /px_unit(539) )
B.append( (abc(1,47)) /px_unit(661) )
##A.append( (abc()+abc()) /px_unit() )
##B.append( (abc()+abc()) /px_unit() )

ts_prob=13.0/16.0#probility of triggering tornado or spiderweb  (success/trials)
ac,de=sum(A)/len(A),sum(B)/len(B)#ratio of speed change by tornado or spiderweb

