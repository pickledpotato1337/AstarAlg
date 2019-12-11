import numpy as np
import Astar as a
import random as ran

class Coordinate:
    def __init__(self, xco, yco):
        self.x=xco
        self.y=yco

test=a.AyStarAlg(10,10);
li=[]
for i in range(20):
    aux=Coordinate(ran.randint(1, 10), ran.randint(1, 10))
    li.append(aux)
    test.SetObstacle(aux.x, aux.y)

test.SetStartPoint(1, 3)

test.SetEndPoint(8, 9)
test.AyStar()
test.RetraceSteps()
print('retrievedvalue: x, y ')
print(test.currentLoc.currentX)
print('//////')
print(test.currentLoc.currentY)
print('Distance')
print('X: ', test.xEnd-test.currentLoc.currentX)
print('Y: ', test.yEnd-test.currentLoc.currentY)
print((test.xEnd-test.currentLoc.currentX) ** 2 + (test.yEnd-test.currentLoc.currentY) ** 2)
print(test.DistanceToGoal(test.currentLoc))


print('----------startpoint 3-------')
print('----------endpoint 4---------')
print('----------habitat------------')
print('-----------------------------')
print(test.habitatArray)
print('-----------------------------')
print('----------road taken 9 ------')
print('----------display------------')
print('-----------------------------')
print(test.displayArray)