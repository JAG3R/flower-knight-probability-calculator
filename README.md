# flower-knight-probability-calculator
This program is for the DMM game-- "Flower Knight Girl", searching for the best passing probability.  

First of all, you need to get the level map.  
You can find the map on Flower Knight Girl wiki (Japanese version).  
Website:
http://xn--eckq7fg8cygsa1a1je.xn--wiki-4i9hs14f.com/index.php?%E3%83%8E%E3%83%BC%E3%83%9E%E3%83%AB  

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
    1. simple version: the number of paths between targets
    2. precise version:Use Paint to get a precise path length.(see remark in the end)
  2. for PART2: PART2 stands for the next target(s) which you might touch.  
    * selector: PART2 has more than 2 targets.  <b>(e.g.  "Sa-1" : [ ? , [ "?" , "?" ] ] )</b>  
![alt tag](https://raw.githubusercontent.com/JAG3R/flower-knight-probability-calculator/master/all%20kind%20of%20targets/selector.png)  
----------------------------------------------------------------------------------------------------------  
      * enemy: PART2 has 1 target.  <b>(e.g. "Ea-1" : [ ? , [ "?" ] ]  )</b>  
![alt tag](https://raw.githubusercontent.com/JAG3R/flower-knight-probability-calculator/master/all%20kind%20of%20targets/enemy.png)  
----------------------------------------------------------------------------------------------------------  
      * changer: PART2 has more than 2 targets.  <b>(e.g. "Ca-1" : [ ? , [ "?" , "?" ] ] )</b>  
![alt tag](https://raw.githubusercontent.com/JAG3R/flower-knight-probability-calculator/master/all%20kind%20of%20targets/changer.png)  
----------------------------------------------------------------------------------------------------------  
      * teleport: PART2 has 1 target.  <b>(e.g. "Ta-1" : [ ? , [ "?" ] ])</b>  
![alt tag](https://raw.githubusercontent.com/JAG3R/flower-knight-probability-calculator/master/all%20kind%20of%20targets/teleport.png)  
----------------------------------------------------------------------------------------------------------  
      * locker: The next target(1),lock target(1)  <b>(e.g. "La-1" : [ ? , [ "?" , "?" ] ] )</b>  
![alt tag](https://raw.githubusercontent.com/JAG3R/flower-knight-probability-calculator/master/all%20kind%20of%20targets/locker.png)  
----------------------------------------------------------------------------------------------------------  
      * button: The next target(1),belonging gate(1)  <b>(e.g. "Ba-1" : [ ? , [ "?" , "?" ] ] )</b>  
![alt tag](https://raw.githubusercontent.com/JAG3R/flower-knight-probability-calculator/master/all%20kind%20of%20targets/button.png)  
----------------------------------------------------------------------------------------------------------  
      * gate: PART2 has 1 target.  <b>(e.g. "Ga-1" : [ ? , [ "?" ] ] )</b>  
![alt tag](https://raw.githubusercontent.com/JAG3R/flower-knight-probability-calculator/master/all%20kind%20of%20targets/gate.png)  
----------------------------------------------------------------------------------------------------------  
      * accel(tornado): PART2 has 1 target.  <b>(e.g. "Aa-1" : [ ? , [ "?" ] ] )</b>  
![alt tag](https://raw.githubusercontent.com/JAG3R/flower-knight-probability-calculator/master/all%20kind%20of%20targets/accel(tornado).png)  
----------------------------------------------------------------------------------------------------------  
      * decel(spiderweb): PART2 has 1 target.  <b>(e.g. "Da-1" : [ ? , [ "?" ] )</b>  
![alt tag](https://raw.githubusercontent.com/JAG3R/flower-knight-probability-calculator/master/all%20kind%20of%20targets/decel(spiderweb).png)  
----------------------------------------------------------------------------------------------------------  
      * end has no PART2.  <b>(e.g. "end" : [ ? ] )</b>  
![alt tag](https://raw.githubusercontent.com/JAG3R/flower-knight-probability-calculator/master/all%20kind%20of%20targets/end.png)  
----------------------------------------------------------------------------------------------------------  
* team_speed:Input your 5 teams mobility. You can also input 4 or 3 teams.(rare to use)  
  If you want to find best mobility:team_speed=\[0,0,0,0,0\]  
* shuffle the order(y/n):  
  y : shuffle your tema order to get a higher probability.  
  n : don't shuffle

* Take level 12-4 for example:  
![alt tag](https://raw.githubusercontent.com/JAG3R/flower-knight-probability-calculator/master/12-4_map.png)
  # fix=[1,0,1,1]  
  # Enemy=8  
  # Changer=0  
  # Locker=[]  
  # Gate=0  
  # INITIAL=["Ea","Sb-1","Eb","Ec"]  
  # EVENT =
  {"Sa-1":[4,["Ef","Sd-1"]],  
  "Sa-2":[3,["Ef","Sd-1"]],  
  "Sb-1" : [4,["Sa-2","Sc-1"]],  
  "Sb-2" : [3,["Sa-2","Sc-1"]],  
  "Sc-1":[2,["Sd-2","Ee-1"]],  
  "Sc-2":[2,["Sd-2","Ee-1"]],  
  "Sd-1":[3,["Eh-2","Eg"]],  
  "Sd-2":[3,["Eh-2","Eg"]],  
  "Se":[1,["Ed","Ee-2","Eh-5"]],  
  "Ea":[2,["Sa-1"]],  
  "Eb":[1,["Sb-2"]],  
  "Ec":[1,["Se"]],  
  "Ed":[1,["Sc-2"]],  
  "Ee-1":[1,["Eh-4"]],  
  "Ee-2":[2,["Eh-4"]],  
  "Ef":[2,["Eh-1"]],  
  "Eg":[1,["Eh-3"]],  
  "Eh-1":[4,["end"]],  
  "Eh-2":[4,["end"]],  
  "Eh-3":[3,["end"]],  
  "Eh-4":[5,["end"]],  
  "Eh-5":[6,["end"]],  
  "end":[2]}  
  # team_speed=\[727,727,727,727,727\]  
  # shuffle the team order=n  

  # result:  
![alt tag](https://raw.githubusercontent.com/JAG3R/flower-knight-probability-calculator/master/12-4_result.png)

* The method of measuring precise path length by Paint:(not recommend,it"s a bit time consuming.)  
First, you need a map which size MUST be 960X640 pixels so that the ratio transfer will be correct.  
Usually, you can find a 960X640 map on wiki. If not 960X640, you have to take snapshot by yourself.  
**Note:The size MUST be 960X640 pixels. If not, the ratio transfer will be incorrect**  
After that, edit the map with Paint.  
Draw a line between two circles in order to measure the length of path.
And you can see the line holds ?X? pixels.  
Input the 2 arguments into the function abc(\*,\*) and that"s the length of the path.  
Last, replace PART1 with (abc(\*,\*)+abc(\*,\*)+...+abc(\*,\*))/P  (P is set as the averaged path)

