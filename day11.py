
import math
import numpy as np
lines = []
times = 1000000
with open('inputaoc.txt') as file:
    for l in file:
        lines.append(l.strip())
xIdx = []
yIdx = []
for y in range(len(lines)):
    lines[y]=list(lines[y])
    if("#" not in lines[y]):
        yIdx.append(y)

for x in range(len(lines[0])):
    hasHash = False
    for y in range(len(lines)):
        if(lines[y][x] == "#"):
            hasHash = True
    if(not hasHash):
        xIdx.append(x)

# while(y < len(lines)):
#     for i in range(len(yIdx)):
#         if(yIdx[i] == y):
#             for h in range(times-1):
#                 line = []
#                 line = dots.copy()
#                 lines.insert(yIdx[i], line)
#                 for j in range(len(yIdx)):
#                     if(j > i):
#                         yIdx[j] = yIdx[j]+1
#     y = y+1
                    


# for y in range(len(lines)):
#     nxIdx = xIdx.copy()
#     x=0  
#     while x < len(lines[y]):
#         for i in range(len(nxIdx)):
#             if(nxIdx[i] == x):
#                 for h in range(times-1):
#                     lines[y].insert(nxIdx[i],".")
#                     for j in range(len(nxIdx)):
#                         if(j > i):
#                             nxIdx[j] = nxIdx[j]+1
       
#         x= x+1

pairs = []

count = 1
for y in range(len(lines)):
    lines[y]=list(lines[y])
    for x in range(len(lines[y])):
        if(lines[y][x]=="#"):
            lines[y][x] = count
            count = count+1

for x in range(1,count):
    for y in range(1,count):
        if(x !=y):
            pair = [x,y]
            pair.sort()
            if(pair not in pairs):
                pairs.append(pair)

dist = []
for p in pairs:
    first = p[0]
    second = p[1]
    for y in range(len(lines)):
        if(first in lines[y]):
            add_f_x = 0
            add_f_y = 0
            for d in yIdx:
                if(int(d)< y):
                    add_f_y = add_f_y+1
            for f in xIdx:
                if(int(f) < lines[y].index(first)):
                    add_f_x = add_f_x+1
            
            y_coord_f = y+(add_f_y*(times-1))
            x_coord_f = lines[y].index(first)+(add_f_x*(times-1))
        if(second in lines[y]):
            add_s_y = 0
            add_s_x = 0
            for d in yIdx:
                if(int(d)< y):
                    add_s_y= add_s_y+1
            for f in xIdx:
                if(int(f) < lines[y].index(second)):
                    add_s_x = add_s_x+1
            y_coord_s = y+(add_s_y*(times-1))
            x_coord_s = lines[y].index(second)+(add_s_x*(times-1))
    a = abs(y_coord_f-y_coord_s)
    b = abs(x_coord_f-x_coord_s)

    dist.append(a+b)

print(sum(dist))
            


