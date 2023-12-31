import numpy as np

out = []
input = []
with open("inaoc.txt") as file:
    for line in file:
        input.append(line.strip())

seed_range = []
for x in range(len(input)):
    if(input[x].split(":")[0] == "seeds"):
        s=0
        while s< len(input[x].split(":")[1].split()):
            sr = range(int(input[x].split(":")[1].split()[s]), int(input[x].split(":")[1].split()[s])+int(input[x].split(":")[1].split()[s+1]))
            seed_range.append(sr)
            s=s+2
loc = []
for s in seed_range:
    new_val = []
    next_val = []
    # print("seeds: " )
    # print(s)
    for x in range(len(input)):
        if(input[x].split(":")[0] == "seed-to-soil map"):
            x=x+1
            overlap = 0
            left = []
            while(input[x] !=''):
                ran_len = int(input[x].split()[2])
                start_des = int(input[x].split()[0])
                start_src =  int(input[x].split()[1])
                rang = range(start_src, start_src+ran_len)
                if(s[0] in rang and s[-1] not in rang):
                        overlap = (range(s[0], rang[-1]+1))
                        diff = overlap[0]-start_src
                        new_val.append(range(start_des+diff, start_des+diff+len(overlap)))
                        left.append(range(rang[-1]+1, s[-1]+1))
                        break
                elif(s[-1] in rang and s[0] not in rang):
                        overlap =(range(rang[0], s[-1]+1))
                        diff = overlap[0]-start_src
                        new_val.append(range(start_des+diff, start_des+diff+len(overlap)))
                        left.append(range(s[0], rang[0]))
                        break
                elif(s[0] in rang and s[-1] in rang):
                        overlap = (s)
                        diff = overlap[0]-start_src
                        new_val.append(range(start_des+diff, start_des+diff+len(overlap)))
                        break
                x = x +1
            if(left != []):
                    for l in left:
                        new_val.append(l)
            if(left == [] and overlap == 0):
                    new_val.append(s)
            # print("soil: " )
            # print(new_val)
        if(input[x].split(":")[0] == "soil-to-fertilizer map"):
            y=x
            while(next_val != [] ):
                x= y+1
                s = next_val.pop()
                overlap = 0
                done = False
                left = []
                while(input[x] !=''):
                    ran_len = int(input[x].split()[2])
                    start_des = int(input[x].split()[0])
                    start_src =  int(input[x].split()[1])
                    rang = range(start_src, start_src+ran_len)
                    if(s[0] in rang and s[-1] not in rang):
                        overlap = (range(s[0], rang[-1]+1))
                        diff = overlap[0]-start_src
                        new_val.append(range(start_des+diff, start_des+diff+len(overlap)))
                        next_val.append(range(rang[-1]+1, s[-1]+1))
                        done = True
                        break
                    elif(s[-1] in rang and s[0] not in rang):
                        overlap =(range(rang[0], s[-1]+1))
                        diff = overlap[0]-start_src
                        new_val.append(range(start_des+diff, start_des+diff+len(overlap)))
                        next_val.append(range(s[0], rang[0]))
                        done = True
                        break
                    elif(s[0] in rang and s[-1] in rang):
                        overlap = (s)
                        diff = overlap[0]-start_src
                        new_val.append(range(start_des+diff, start_des+diff+len(overlap)))
                        done = True
                        break
                    x = x +1
                if(not done):
                    new_val.append(s)
            # print("fert: ")
            # print(new_val)
        if(input[x].split(":")[0] == "fertilizer-to-water map"):
            y=x
            while(new_val != [] ):
                x= y+1
                s = new_val.pop()
                overlap = 0
                done = False
                left = []
                while(input[x] !=''):
                    ran_len = int(input[x].split()[2])
                    start_des = int(input[x].split()[0])
                    start_src =  int(input[x].split()[1])
                    rang = range(start_src, start_src+ran_len)
                    if(s[0] in rang and s[-1] not in rang):
                        overlap = (range(s[0], rang[-1]+1))
                        diff = overlap[0]-start_src
                        next_val.append(range(start_des+diff, start_des+diff+len(overlap)))
                        new_val.append(range(rang[-1]+1, s[-1]+1))
                        done = True
                        break
                    elif(s[-1] in rang and s[0] not in rang):
                        overlap =(range(rang[0], s[-1]+1))
                        diff = overlap[0]-start_src
                        next_val.append(range(start_des+diff, start_des+diff+len(overlap)))
                        new_val.append(range(s[0], rang[0]))
                        done = True
                        break
                    elif(s[0] in rang and s[-1] in rang):
                        overlap = (s)
                        diff = overlap[0]-start_src
                        next_val.append(range(start_des+diff, start_des+diff+len(overlap)))
                        done = True
                        break
                    x = x +1
                if(not done):
                    next_val.append(s)
            # print("wat: ")
            # print(next_val)
        if(input[x].split(":")[0] == "water-to-light map"):
            y=x
            while(next_val != [] ):
                x= y+1
                s = next_val.pop()
                overlap = 0
                done = False
                left = []
                while(input[x] !=''):
                    ran_len = int(input[x].split()[2])
                    start_des = int(input[x].split()[0])
                    start_src =  int(input[x].split()[1])
                    rang = range(start_src, start_src+ran_len)
                    if(s[0] in rang and s[-1] not in rang):
                        overlap = (range(s[0], rang[-1]+1))
                        diff = overlap[0]-start_src
                        new_val.append(range(start_des+diff, start_des+diff+len(overlap)))
                        done = True
                        next_val.append(range(rang[-1]+1, s[-1]+1))
                        break
                    elif(s[-1] in rang and s[0] not in rang):
                        overlap =(range(rang[0], s[-1]+1))
                        diff = overlap[0]-start_src
                        new_val.append(range(start_des+diff, start_des+diff+len(overlap)))
                        next_val.append(range(s[0], rang[0]))
                        done = True
                        break
                    elif(s[0] in rang and s[-1] in rang):
                        overlap = (s)
                        diff = overlap[0]-start_src
                        new_val.append(range(start_des+diff, start_des+diff+len(overlap)))
                        done = True
                        break
                    x = x +1
                if(not done):
                    new_val.append(s)
            # print("light: ")
            # print(new_val)
        if(input[x].split(":")[0] == "light-to-temperature map"):
            y=x
            while(new_val != [] ):
                x= y+1
                s = new_val.pop()
                overlap = 0
                done = False
                left = []
                while(input[x] !=''):
                    ran_len = int(input[x].split()[2])
                    start_des = int(input[x].split()[0])
                    start_src =  int(input[x].split()[1])
                    rang = range(start_src, start_src+ran_len)
                    if(s[0] in rang and s[-1] not in rang):
                        overlap = (range(s[0], rang[-1]+1))
                        diff = overlap[0]-start_src
                        next_val.append(range(start_des+diff, start_des+diff+len(overlap)))
                        new_val.append(range(rang[-1]+1, s[-1]+1))
                        done = True
                        break
                    elif(s[-1] in rang and s[0] not in rang):
                        overlap =(range(rang[0], s[-1]+1))
                        diff = overlap[0]-start_src
                        next_val.append(range(start_des+diff, start_des+diff+len(overlap)))
                        new_val.append(range(s[0], rang[0]))
                        done = True
                        break
                    elif(s[0] in rang and s[-1] in rang):
                        overlap = (s)
                        diff = overlap[0]-start_src
                        next_val.append(range(start_des+diff, start_des+diff+len(overlap)))
                        done = True
                        break
                    x = x +1
                if(not done):
                    next_val.append(s)
            # print("temp: ")
            # print(next_val)
        if(input[x].split(":")[0] == "temperature-to-humidity map"):
            y=x
            while(next_val != [] ):
                x= y+1
                s = next_val.pop()
                done = False
                overlap = 0
                left = []
                while(x < len(input) and input[x] !=''):
                    ran_len = int(input[x].split()[2])
                    start_des = int(input[x].split()[0])
                    start_src =  int(input[x].split()[1])
                    rang = range(start_src, start_src+ran_len)
                    if(s[0] in rang and s[-1] not in rang):
                        overlap = (range(s[0], rang[-1]+1))
                        diff = overlap[0]-start_src
                        new_val.append(range(start_des+diff, start_des+diff+len(overlap)))
                        next_val.append(range(rang[-1]+1, s[-1]+1))
                        done = True
                        break
                    elif(s[-1] in rang and s[0] not in rang):
                        overlap =(range(rang[0], s[-1]+1))
                        diff = overlap[0]-start_src
                        new_val.append(range(start_des+diff, start_des+diff+len(overlap)))
                        next_val.append(range(s[0], rang[0]))
                        done = True
                        break
                    elif(s[0] in rang and s[-1] in rang):
                        overlap = (s)
                        diff = overlap[0]-start_src
                        new_val.append(range(start_des+diff, start_des+diff+len(overlap)))
                        done = True
                        break
                    x = x +1
                if(not done):
                    new_val.append(s)
            # print("hum: ")
            # print(new_val)
        if(input[x].split(":")[0] == "humidity-to-location map"):
            y=x
            while(new_val != [] ):
                x= y+1
                s = new_val.pop()
                done = False
                overlap = 0
                left = []
                while(x < len(input) and input[x] !=''):
                    ran_len = int(input[x].split()[2])
                    start_des = int(input[x].split()[0])
                    start_src =  int(input[x].split()[1])
                    rang = range(start_src, start_src+ran_len)
                    if(s[0] in rang and s[-1] not in rang):
                        overlap = (range(s[0], rang[-1]+1))
                        diff = overlap[0]-start_src
                        next_val.append(range(start_des+diff, start_des+diff+len(overlap)))
                        new_val.append(range(rang[-1]+1, s[-1]+1))
                        done = True
                        break
                    elif(s[-1] in rang and s[0] not in rang):
                        overlap =(range(rang[0], s[-1]+1))
                        diff = overlap[0]-start_src
                        next_val.append(range(start_des+diff, start_des+diff+len(overlap)))
                        new_val.append(range(s[0], rang[0]))
                        done = True
                        break
                    elif(s[0] in rang and s[-1] in rang):
                        overlap = (s)
                        diff = overlap[0]-start_src
                        next_val.append(range(start_des+diff, start_des+diff+len(overlap)))
                        done = True
                        break
                    x = x +1
                if(not done):
                    next_val.append(s)
   #         print("loc: ")
  #          print(next_val)
            loc.append(next_val)
 #   print("\n")
#print(loc)
flat_list = [item for sublist in loc for item in sublist]
#print(flat_list)
lowest = float('inf')
for x in flat_list:
    if(x[0] < lowest):
        lowest = x[0]

print(lowest)

            


