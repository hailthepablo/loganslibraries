class Grid:
    def __init__(self,array,origin=(0,0),order="yx",xDir="right",yDir="down"):
        self.array = array
        self.origin = origin
        self.order = order
        self.width = len(self.array[0])
        self.height = len(self.array)
        
        if self.order == "yx":
            self.slot0 = 0
            self.slot1 = 1
        elif self.order == "xy":
            self.slot1 = 0
            self.slot0 = 1
        else:
            raise ValueError("Attribute 'order' can only be either xy or yx.")
        
        if xDir == "right":
            self.xDir = 1
        elif xDir == "left":
            self.xDir = -1
        else:
            raise ValueError("Attribute 'xDir' can only be either left or right.")

        if yDir == "down":
            self.yDir = 1
        elif yDir == "up":
            self.yDir = -1
        else:
            raise ValueError("Attribute 'yDir' can only be either up or down.")
        
    def getPos(self,indexes):
        if self.order == "yx":
            return (self.yDir*(indexes[0]-self.origin[0]),self.xDir*(indexes[1]-self.origin[1]))
        elif self.order == "xy":
            return (self.xDir*(indexes[1]-self.origin[1]),self.yDir*(indexes[0]-self.origin[0]))

    def displayLists(self):
        for i in self.array:
            print(i)

    def getElem(self,pos):
        rowNum = self.yDir*pos[self.slot0]+self.origin[0]
        columnNum = self.xDir*pos[self.slot1]+self.origin[1]
        if (0 <= rowNum) and (rowNum <= self.height-1) and (0 <= columnNum) and (columnNum <= self.width-1):
            return self.array[rowNum][columnNum]
        else:
            return None

    def setElem(self,pos,elem):
        rowNum = self.yDir*pos[self.slot0]+self.origin[0]
        columnNum = self.xDir*pos[self.slot1]+self.origin[1]
        if (0 <= rowNum) and (rowNum <= self.height-1) and (0 <= columnNum) and (columnNum <= self.width-1):
            self.array[self.yDir*pos[self.slot0]+self.origin[0]][self.xDir*pos[self.slot1]+self.origin[1]] = elem

    def getDisplayArray(self,align="left"):
        if not (align in ["left","right"]):
            raise ValueError("Parameter 'align' can only be either left or right.")
        maxList = []
        for i in range(self.width):
            curMax = 0
            for j in range(self.height):
                if len(str(self.array[j][i])) > curMax:
                    curMax = len(str(self.array[j][i]))
            maxList += [curMax]
        
        displayArray = [["." for j in range(self.width)] for i in range(self.height)]
        for i in range(self.width):
            for j in range(self.height):
                spaces = " "*(maxList[i]-len(str(self.array[j][i])))
                if align == "left":
                    displayArray[j][i] = str(self.array[j][i]) + spaces
                elif align == "right":
                    displayArray[j][i] = spaces + str(self.array[j][i])
        return displayArray