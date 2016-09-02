from auto_run import*
fix=[0,1,1,0,0,0]
Enemy,Changer,Locker,Gate=9,5,[1],1
INITIAL=['Aa-1','Ba','Bc','Bd','La-1','Ac']
EVENT ={'Ea':[abc(80,1),['Tf']],
        'Eb':[abc(80,1),['Ta']],
        'Ec':[abc(80,1),['Tc']],
        'Ed':[abc(80,1),['Cd']],
        'Ee':[abc(80,1),['Th']],
        'Ef':[abc(80,1),['Th']],
        'Eg':[abc(80,1),['Ti']],
        'Eh':[abc(80,1),['Ti']],
        'Ei':[abc(80,1)*3,['Tg']],
        'Ca':[abc(80,1)*2,['Ee','Ef']],
        'Cb':[abc(80,1),['Bb','Ab']],
        'Cc':[abc(80,1),['Eg','Eh']],
        'Cd':[abc(80,1),['Te','Td']],
        'Ce':[0,['Ga','Bd']],
        'Ta':[abc(80,1)*2,['Ca']],
        'Tb':[abc(80,1)*2,['La-2']],
        'Tc':[abc(80,1)*2,['Cc']],
        'Td':[abc(80,1),['end']],
        'Te':[abc(80,1)*2,['Ca']],
        'Tf':[abc(80,1),['Ca']],
        'Tg':[abc(80,1)*5,['end']],
        'Th':[abc(80,1),['Aa-2']],
        'Ti':[abc(80,1),['La-2']],
        'La-1':[abc(80,1),['Ce','Ga']],
        'La-2':[abc(80,1)*2,['Ce','Ga']],
        'Ba':[abc(80,1)*3,['Eb','Ga']],
        'Bb':[abc(80,1)*2,['Ec','Ga']],
        'Bc':[abc(80,1),['Ea','Ga']],
        'Bd':[abc(80,1),['Ad','Ga']],
        'Ga':[abc(80,1),['Ae']],
        'Aa-1':[abc(80,1),['Cb']],
        'Aa-2':[abc(80,1)*2,['Cb']],
        'Ab':[abc(80,1),['Tb']],
        'Ac':[abc(80,1),['Bb']],
        'Ad':[abc(80,1)*2,['Ed']],
        'Ae':[abc(80,1),['Ei']],
        'end':[abc(80,1)*3]}
team_speed,shuffle=[500,600,645,321,483],False#
auto(fix,len(team_speed),EVENT,team_speed,shuffle,Enemy,Changer,Locker,Gate,INITIAL)
#if find best:team_speed=[0,0,0,0,0],True#

