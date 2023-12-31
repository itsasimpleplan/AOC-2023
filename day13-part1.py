import numpy as np
sketches = []
with open('inaoc.txt') as file:
    lines = file.readlines()
    x=0
    while x in range(len(lines)):
        sketch = []
        while x < len(lines) and lines[x] != "\n":
            sketch.append(list(lines[x].strip()))
            x = x+1
        x = x+1
        sketches.append(sketch)
def listComp(list1, list2):
    for x in range(len(list1)):
        if(list1[x] != list2[x]):
            return False
    return True

def checkRowSim(sketch, rowNum):
    checkNum = rowNum+1
    before = checkNum
    after = len(sketch) - (checkNum)
    if(before != after):
        before = min(before,after)
        after= before
    simSketch = []
    simSketch = sketch[checkNum-after:checkNum+after]
    simrows = 0
    half = len(simSketch)//2
    for x in range(len(simSketch)//2):
        if(not listComp(simSketch[(half-1)-x], simSketch[half+x])):
            return False
    if(simSketch != []):
        return True
    else:
        return False
    
def checkColSim(sketch, rowNum):
    checkNum = rowNum+1
    before = checkNum
    after = len(sketch) - (checkNum)
    if(before != after):
        before = min(before,after)
        after= before
    simSketch= []
    simSketch = sketch[checkNum-after:checkNum+after]
    simrows = 0
    half = len(simSketch)//2
    for x in range(len(simSketch)//2):
        if(not listComp(simSketch[(half-1)-x], simSketch[half+x])):
            return False
    if(simSketch.tolist() != []):
        return True
    else:
        return False


colSims = []
rowSims = []
for sketch in sketches:
    for row in range(len(sketch)):
        if(checkRowSim(sketch, row)):
            rowSims.append(row+1)
            print("row sim " + str(row))
    transSketch = np.array(sketch).T
    for row in range(len(transSketch)):
            if(checkColSim(transSketch, row)):
                colSims.append(row+1)
                print("Col sim " + str(row))

sum = 0
for x in colSims:
    sum = sum +x
for x in rowSims:
    sum = sum + (100*x)
print("Sum " + str(sum))         


            

    