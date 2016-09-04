# flower-knight-probability-calculator
This program is for the DMM game-- "Flower Knight Girl", searching for the best passing probability.  

First of all, you need to get the level map.  
You can find the map on Flower Knight Girl wiki (Japanese version).  
Website:
http://xn--eckq7fg8cygsa1a1je.xn--wiki-4i9hs14f.com/index.php?%E3%83%95%E3%83%A9%E3%83%AF%E3%83%BC%E3%83%8A%E3%82%A4%E3%83%88%E3%82%AC%E3%83%BC%E3%83%AB%E6%94%BB%E7%95%A5%E3%81%BE%E3%81%A8%E3%82%81wiki  

Use Paint to edit the map, you need to remark all the targets of the map. You can check all kinds of targets file to see all the targets.  
After that, you need to input the following datas:  
* fix: the least team arangement to avoid 0% pass  
* Enemy:number of enemies  
* Changer:number of changers  
* Locker:the numbers on each lockers (If no lockers, input \[\])  
* Gate:number of gates  
* INITIAL:initial targets for each camps  
* EVENT:  
There may be more than 1 path that come into the target.  
In this case, append -1,-2 after the target to enumerate it.  
Each target has two PARTs--[PART1,[PART2]]  
  1. for PART1: PART1 stands for the distance to reach the target.  
    1. simple version: P\*count (where count is the number of paths between targets) #P is the average path length. I have set it  
    2. precise version:Use Paint to get a precise path length.(see remark in the end)
  2. for PART2: PART2 stands for the next target(s) which you might touch.  
    * selector: List all the next targets that this selector would go to.  
    * enemy: The next target(1)  
    * changer: List all the next targets that this changer would go to.  
    * teleport: The next target(1)  
    * locker: The next target(1),lock target(1)  
    * button: The next target(1),belonging gate(1)  
    * gate: The next target(1)  
    * accel(tornado): The next target(1)  
    * decel(spiderweb): The next target(1)  
    * end has no PART2.  
* team_speed:Input your 5 teams mobility. You can also input 4 or 3 teams.(rare to use)  
  If you want to find best mobility:team_speed=\[0,0,0,0,0\]  
* shuffle=False:
  If you want to get a higher probability(may spend a little bit longer time), shuffle=True

* Take level 12-4 for example:  
![alt tag](https://raw.githubusercontent.com/JAG3R/flower-knight-probability-calculator/master/12-4(example).png)
  # fix=[1,0,1,1]  
  # Enemy=8  
  # Changer=0  
  # Locker=[]  
  # Gate=0  
  # INITIAL=['Ea','Sb-1','Eb','Ec']  
  # EVENT =
  {'Sa-1':[P\*4,['Ef','Sd-1']],  
  'Sa-2':[P\*3,['Ef','Sd-1']],  
  'Sb-1' : [P\*4,['Sa-2','Sc-1']],  
  'Sb-2' : [P\*3,['Sa-2','Sc-1']],  
  'Sc-1':[P\*2,['Sd-2','Ee-1']],  
  'Sc-2':[P\*2,['Sd-2','Ee-1']],  
  'Sd-1':[P\*3,['Eh-2','Eg']],  
  'Sd-2':[P\*3,['Eh-2','Eg']],  
  'Se':[P\*1,['Ed','Ee-2','Eh-5']],  
  'Ea':[P\*2,['Sa-1']],  
  'Eb':[P\*1,['Sb-2']],  
  'Ec':[P\*1,['Se']],  
  'Ed':[P\*1,['Sc-2']],  
  'Ee-1':[P\*1,['Eh-4']],  
  'Ee-2':[P\*2,['Eh-4']],  
  'Ef':[P\*2,['Eh-1']],  
  'Eg':[P\*1,['Eh-3']],  
  'Eh-1':[P\*4,['end']],  
  'Eh-2':[P\*4,['end']],  
  'Eh-3':[P\*3,['end']],  
  'Eh-4':[P\*5,['end']],  
  'Eh-5':[P\*6,['end']],  
  'end':[P\*2]}  
  # team_speed=\[727,727,727,727,727\]  
  # shuffle=False  

  # result:  
![alt tag](https://raw.githubusercontent.com/JAG3R/test/master/12-4.png)

* The method of measuring precise path length by Paint:(not recommend,it's a bit time consuming.)  
First, you need a map which size MUST be 960X640 pixels so that the ratio transfer will be correct.  
Usually, you can find a 960X640 map on wiki. If not 960X640, you have to take snapshot by yourself.  
**Note:The size MUST be 960X640 pixels. If not, the ratio transfer will be incorrect**  
After that, edit the map with Paint.  
Draw a line between two circles in order to measure the length of path.
And you can see the line holds ?X? pixels.  
Input the 2 arguments into the function abc(\*,\*) and that's the length of the path.  
Last, replace PART1 with abc(\*,\*)+abc(\*,\*)+...+abc(\*,\*)

