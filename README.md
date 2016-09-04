# flower-knight-probability-calculator
This program is for the DMM game-- "Flower Knight Girl", searching for the best passing probability.
After editing the main.py, run.

Editing main.py:
First of all, you need to get a snapshot of the level map.
And the size MUST be 960X640 pixels so that the ratio transfer will be correct.
You can find the map on Flower Knight Girl wiki (Japanese version).

Website:
http://xn--eckq7fg8cygsa1a1je.xn--wiki-4i9hs14f.com/index.php?%E3%83%95%E3%83%A9%E3%83%AF%E3%83%BC%E3%83%8A%E3%82%A4%E3%83%88%E3%82%AC%E3%83%BC%E3%83%AB%E6%94%BB%E7%95%A5%E3%81%BE%E3%81%A8%E3%82%81wiki

Note:Usually, the size MUST be 960X640 pixels. If not, you have to take a screenshot by yourself.

Take level 12-4 for example:
First, you need to remark all the targets of the map. You can check all kinds of targets file to see all the targets.
![alt tag](https://raw.githubusercontent.com/JAG3R/flower-knight-probability-calculator/master/12-4(example).png)
After that, you need to input the following datas:
fix: the least team arangement to avoid 0% pass
Enemy:number of enemies
Changer:number of changers
Locker:the numbers on each lockers (If no lockers, just remove the '?')
Gate:number of gates
INITIAL:initial targets for each camps

Rules of EVENT:

There may be more than 1 path that come into the target.
In this case, append -1,-2 after the target to enumerate it.
Each target has two PARTs--[PART1,[PART2]]
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

e.g. level 12-4</br>
EVENT ={'Sa-1':[P*4,['Ef','Sd-1']],#selector  
		'Sa-2':[P*3,['Ef','Sd-1']],</br>
		'Sb-1':[P*4,['Sa-2','Sc-1']],</br>
		'Sb-2':[P*3,['Sa-2','Sc-1']],</br>
		'Sc-1':[P*2,['Sd-2','Ee-1']],</br>
		'Sc-2':[P*2,['Sd-2','Ee-1']],</br>
		'Sd-1':[P*3,['Eh-2','Eg']],</br>
		'Sd-2':[P*3,['Eh-2','Eg']],</br>
		'Se':[P*1,['Ed','Ee-2','Eh-5']],</br>
		'Ea':[P*2,['Sa-1']],#enemy</br>
		'Eb':[P*1,['Sb-2']],</br>
		'Ec':[P*1,['Se']],</br>
		'Ed':[P*1,['Sc-2']],</br>
		'Ee-1':[P*1,['Eh-4']],</br>
		'Ee-2':[P*2,['Eh-4']],</br>
		'Ef':[P*2,['Eh-1']],</br>
		'Eg':[P*1,['Eh-3']],</br>
		'Eh-1':[P*4,['end']],</br>
		'Eh-2':[P*4,['end']],</br>
		'Eh-3':[P*3,['end']],</br>
		'Eh-4':[P*5,['end']],</br>
		'Eh-5':[P*6,['end']],</br>
		'end':[P*2]</br>
        }

