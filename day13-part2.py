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
def to_matrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

colSims = []
rowSims = []
for sketch in sketches:
    colSim = -1
    rowSim = -1
    for row in range(len(sketch)):
        if(checkRowSim(sketch, row)):
            rowSim = row+1
          #  print("Row sim " + str(row))  
    transSketch = np.array(sketch).T
    for row in range(len(transSketch)):
            if(checkColSim(transSketch, row)):
                colSim = row+1
             #   print("Col sim " + str(row))
    count = 0

    # print(colSim)
    # print(rowSim)
    flat_sketch = [item for sublist in sketch for item in sublist]
    isChanged = False
    while count < len(sketch)*len(sketch[0]):
        if(flat_sketch[count] == "#"):
            flat_sketch[count] = "."
        elif(flat_sketch[count] == "."):
            flat_sketch[count] = "#"
        new_sketch = to_matrix(flat_sketch, len(sketch[0]))

        for row in range(len(new_sketch)):
                if(checkRowSim(new_sketch, row)):
                    if rowSim >= 0 and rowSim != (row+1) and not isChanged:
                        rowSim = row+1
                        isChanged = True
                    elif colSim >=0 and not isChanged:
                        rowSim = row+1
                        isChanged = True
                        colSim = -1
                      #  print("New row sim - no col sim " + str(row))  
        transSketch = np.array(new_sketch).T
        for row in range(len(transSketch)):
                if(checkColSim(transSketch, row)):
                    if colSim >= 0 and colSim != (row+1) and not isChanged:
                        colSim = row+1
                        isChanged = True
                    elif rowSim >=0 and not isChanged:
                        colSim = row+1
                        isChanged = True
                        rowSim = -1
        
        if(flat_sketch[count] == "#"):
            flat_sketch[count] = "."
        elif(flat_sketch[count] == "."):
            flat_sketch[count] = "#"
        count = count+1
    # print(colSim)
    # print(rowSim)
    if(colSim>=0):
        colSims.append(colSim)
    if(rowSim>=0):
        rowSims.append(rowSim)

    
# print(colSims)
# print(rowSims)

sum = 0
for x in colSims:
    sum = sum +x
for x in rowSims:
    sum = sum + (100*x)
print("Sum " + str(sum))         


            

    