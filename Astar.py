import numpy as np
import math as mt




class Tile:
    def __init__(self, xPos, yPos):
        self.currentX=xPos
        self.currentY=yPos
        self.previousTile=None
        self.heuRoad=0
        self.distanceMade=0


    def Set(self, xPos, yPos):
        self.currentX=xPos
        self.currentY=yPos

    def IncreaseRoadTaken(self):
        self.distanceMade+=1



    def GetTotalDistance(self):
        return self.distanceMade+self.heuRoad

    def SetDistance(self, heuristicDistance):
        self.heuRoad=heuristicDistance

    def SetParent(self, ancestor):
        self.previousTile=ancestor
        self.distanceMade += ancestor.distanceMade


    #define 8 directions of movement
    def GoN(self):

        self.currentX-=1
        self.IncreaseRoadTaken()

    def GoNW(self):

        self.currentX-=1
        self.currentY-=1
        self.IncreaseRoadTaken()

    def GoW(self):
        self.currentY-= 1
        self.IncreaseRoadTaken()

    def GoSW(self):
        self.currentY-=1
        self.currentX+=1
        self.IncreaseRoadTaken()

    def GoS(self):
        self.currentX+=1
        self.IncreaseRoadTaken()

    def GoSE(self):
        self.currentX += 1
        self.currentY += 1
        self.IncreaseRoadTaken()

    def GoE(self):
        self.currentY+=1
        self.IncreaseRoadTaken()

    def GoNE(self):
        self.currentY += 1
        self.currentX -= 1
        self.IncreaseRoadTaken()


class AyStarAlg:


    def __init__(self, xSize, ySize):

        self.xAxis=xSize
        self.yAxis=ySize
        coordinates=(xSize, ySize)
        self.habitatArray=np.ones(coordinates)
        self.habitatArray=np.pad(self.habitatArray, pad_width=1, mode="constant", constant_values=0)
        self.displayArray=self.habitatArray
        self.candidates=list()
        self.closedList=list()
        self.xStart=1
        self.yStart=1
        self.xEnd=1
        self.yEnd=1

        self.currentLoc=Tile(self.xStart, self.yStart,)

        self.distanceMade=0

    def SetObstacle(self, xPos, yPos):
        self.habitatArray[xPos,yPos]=0
        self.displayArray[xPos,yPos]=0


    def SetEndPoint(self, xDes, yDes):
        if self.habitatArray[xDes,yDes]!=0:
            self.habitatArray[xDes, yDes]=4
            self.xEnd=xDes
            self.yEnd=yDes


    def SetStartPoint(self, xSt, ySt):

            self.habitatArray[xSt, ySt]=3
            self.xStart=xSt
            self.yStart=ySt
            self.currentLoc.Set(xSt, ySt)


    def DistanceToGoal(self, Scoutingtile):
        xdistance = (self.xEnd - Scoutingtile.currentX) ** 2
        ydistance = (self.yEnd - Scoutingtile.currentY) ** 2
        rval = xdistance + ydistance
        return  rval**0.5


    def GetLocValue(self, localtile):
        return(self.habitatArray[localtile.currentX,localtile.currentY])


    def RetraceSteps(self):
        self.habitatArray[self.xStart, self.yStart] = 3
        self.displayArray[self.xStart, self.yStart] = 3
        self.closedList.reverse()
        while(self.GetLocValue(self.currentLoc)!=3):
            if(len(self.closedList)>0):
                self.currentLoc=self.closedList.pop(0)
                self.displayArray[self.currentLoc.currentX, self.currentLoc.currentY]=9
                print("tracing from %d-%d coordinates"%(self.currentLoc.currentX, self.currentLoc.currentY))
            else:
                return


    #Obsolete
    def IsOnClosedList(self, inqTile):
        for i in self.closedList:
            if inqTile.currentX==i.currentX & inqTile.currentY==i.currentY:
                return 1

        return 0
    #Obsolete
    def IsOnCandidates(self, inqTile):
        #prevents from multiple declarations of same tile
        for i in self.candidates:
            if inqTile.currentX == i.currentX & inqTile.currentY == i.currentY:
                return 1
        return 0

    def GetIndexofSmallest(self, list):
        aux=list[0]
        aux2=0
        for i in range(len(list)):
            if(list[i]<aux):
                aux=list[i]
                aux2=i
        return aux2

    def Exploration(self, scout):
        #print('scout coordinates: %d - %d' % (scout.currentX, scout.currentY))
        if self.GetLocValue(scout) == 1 or self.GetLocValue(scout) == 4:
                    distance = self.DistanceToGoal(scout)
                    scout.SetDistance(distance)
                    scout.SetParent(self.currentLoc)
                    self.candidates.append(scout)
                    if self.habitatArray[scout.currentX, scout.currentY] != 4:
                        self.habitatArray[scout.currentX, scout.currentY] = 5
                        self.displayArray[scout.currentX, scout.currentY] = 5



    def GetCandidates(self):
        # creates list of candidate tiles, sadly
        # needs protection from going off-grid
        # needs protection from going into closedlist
        # needs check preventing from multiple candidate insertion


        xCoordinate = self.currentLoc.currentX
        yCoordinate = self.currentLoc.currentY

        #declare new tile for every step
        ScoutingTileN = Tile(xCoordinate, yCoordinate)
        ScoutingTileN.GoN()
        self.Exploration(ScoutingTileN)
        #print('currentloc coordinates 1: ', self.currentLoc.currentX, self.currentLoc.currentY)

        ScoutingTileNW = Tile(xCoordinate, yCoordinate)
        ScoutingTileNW.GoNW()
        #print('currentloc coordinates 2:', self.currentLoc.currentX, self.currentLoc.currentY)
        self.Exploration(ScoutingTileNW)

        ScoutingTileW = Tile(xCoordinate, yCoordinate)
        ScoutingTileW.GoW()
        self.Exploration(ScoutingTileW)

        ScoutingTileSW = Tile(xCoordinate, yCoordinate)
        ScoutingTileSW.GoSW()
        self.Exploration(ScoutingTileSW)

        ScoutingTileS = Tile(xCoordinate, yCoordinate)
        ScoutingTileS.GoS()
        self.Exploration(ScoutingTileS)

        ScoutingTileSE = Tile(xCoordinate, yCoordinate)
        ScoutingTileSE.GoSE()
        self.Exploration(ScoutingTileSE)

        ScoutingTileE = Tile(xCoordinate, yCoordinate)
        ScoutingTileE.GoE()
        self.Exploration(ScoutingTileE)

        ScoutingTileNE = Tile(xCoordinate, yCoordinate)
        ScoutingTileNE.GoNE()
        self.Exploration(ScoutingTileNE)



    def AyStar(self):

        print('initialisation')
        print('loc value', self.GetLocValue(self.currentLoc))
        print('loc coordinates',self.currentLoc.currentX, '-', self.currentLoc.currentY)
        print('approx distance ',self.DistanceToGoal(self.currentLoc))
        print('candidates: %d '%(len(self.candidates)))
        print('getting candidates')
        self.GetCandidates()
        #so, without further ado
        while self.GetLocValue(self.currentLoc)!=4:
            if len(self.candidates)!=0:
                self.closedList.append(self.currentLoc)
                self.habitatArray[self.currentLoc.currentX, self.currentLoc.currentY] = 6
                openCosts=[i.GetTotalDistance() for i in self.candidates]
                wantedIndex=self.GetIndexofSmallest(openCosts)
                self.currentLoc = self.candidates[wantedIndex]
                constraint = self.GetLocValue(self.currentLoc)
                if constraint == 4:
                    break
                del self.candidates[wantedIndex]
                #remove the candidate from list, retard. fix the comparator.
                self.GetCandidates()
                #print('a* loop in effect')
                #print('loc value', self.GetLocValue(self.currentLoc))
                #print('loc coordinates', self.currentLoc.currentX, '-', self.currentLoc.currentY)
                print('candidate index is %d' % (wantedIndex))
            else:
                print('ran out of candidates')
                return

        print('found ')



