import math
###This module is aiming to transfering the mobility into pixels on Paint###
'''If you want to get a more precise data,go to wiki and download the map or take screenshot.(MUST 960X640 pixels!!!!!!)
Edit the map by Paint. Draw a line between circles and you can see the line holds ?x? pixels.
Input the 2 arguments into the function--abc(,) and you can get the length of it.
The more datas you input, the more precise it is!!'''
#======================================================#
##c**2=a**2+b**2
def abc(a,b):
    return math.sqrt(a**2+b**2)
#======================================================#
#average length of a path
path=[abc(81,18),abc(88,10),abc(87,13),abc(133,9),abc(92,30),abc(96,6),abc(85,23),abc(73,70),abc(45,113),abc(61,65),abc(80,30),abc(75,18),abc(51,45),abc(116,3),abc(70,22),abc(80,24),abc(74,1),abc(93,1),abc(19,89),abc(68,57),abc(117,17),abc(64,32),abc(41,46),abc(58,58),abc(33,65),abc(60,46),abc(58,82),abc(58,42),abc(83,26),abc(130,69),abc(86,8),abc(15,81),abc(140,1),abc(80,1),abc(95,1),abc(43,70),abc(68,38),abc(80,40),abc(84,11),abc(36,61),abc(60,39),abc(73,72),abc(79,6),abc(84,16),abc(6,61),abc(129,1),abc(30,76),abc(59,50),abc(40,75),abc(91,76),abc(48,87),abc(11,154),abc(100,47)]
P=sum(path)/len(path)
#======================================================#
##transfering mobility into pixels
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
#======================================================#
##probility of triggering tornado or spiderweb(success/trials)
ts_prob=13.0/16.0
##measuring the ratio of accelerating(by tornado) or decelerating(by spiderweb)
A,B=[],[]
A.append( (abc(36,40)+abc(89,18)+abc(109,8)+abc(20,2)) / (abc(52,49)+abc(45,74)+abc(22,9)) )
B.append( (abc(45,1)) / (abc(81,43)+abc(30,112)) )
A.append( (abc(76,79)+abc(95,17)+abc(36,3)) /px_unit(539) )
B.append( (abc(1,47)) /px_unit(661) )
##A.append( (abc()+abc()) /px_unit() )
##B.append( (abc()+abc()) /px_unit() )

ac,de=sum(A)/len(A),sum(B)/len(B)#ac:accel,de:decel

