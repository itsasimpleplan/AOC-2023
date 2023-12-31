platform = []
with open("in14.txt") as file:
    for line in file:
        platform.append(list(line.strip()))

def roll_north(platform):
    for row in range(len(platform)):
        for col in range(len(platform[row])):
            if platform[row][col]=="O":
                rows_up = 0
                while row-(rows_up+1)>=0 and platform[row-(rows_up+1)][col] != "#" and platform[row-(rows_up+1)][col] != "O":
                    rows_up = rows_up+1
                platform[row][col] = "."
                platform[row-rows_up][col] = "O"
    return platform

def roll_south(platform):
    for row in range(len(platform)):
        for col in range(len(platform[row])):
            cor_row = (len(platform)-1)-row
            if platform[cor_row][col]=="O":
                
                rows_up = 0
                while cor_row-(rows_up+1)>=0 and platform[cor_row-(rows_up+1)][col] != "#" and platform[cor_row-(rows_up+1)][col] != "O":
                    rows_up = rows_up+1
                platform[cor_row][col] = "."
                platform[cor_row-rows_up][col] = "O"
    return platform
    
def roll_west(platform):
    for row in range(len(platform)):
        for col in range(len(platform[row])):
            if platform[row][col]=="O":
                rows_up = 0
                while col-(rows_up+1)>=0 and platform[row][col-(rows_up+1)] != "#" and platform[row][col-(rows_up+1)] != "O":
                    rows_up = rows_up+1
                platform[row][col] = "."
                platform[row][col-rows_up] = "O"
    return platform

def roll_east(platform):
    for row in range(len(platform)):
        for col in range(len(platform[row])):
            cor_col = (len(platform[row])-1)-col
            if platform[row][cor_col]=="O":
                rows_up = 0
                while cor_col+(rows_up+1)<len(platform[row]) and platform[row][cor_col+(rows_up+1)] != "#" and platform[row][cor_col+rows_up+1] != "O":
                    rows_up = rows_up+1
                platform[row][cor_col] = "."
                platform[row][cor_col+rows_up] = "O"
    return platform

def roll_cycle(platform):
    platform = roll_north(platform)
    platform = roll_west(platform)
    platform = roll_south(platform)
    platform = roll_east(platform)
    return platform

def calc_load(platform):
    load = 0
    for row in range(len(platform)):
        for col in range(len(platform[row])):
            if platform[row][col]=="O":
                load= load +  (len(platform) - row)
    return load
x=0

for x in range(4):
    platform = roll_cycle(platform)
    if(x%10000000 == 0):
        print(x)
    for y in platform:
        print(y)
    print("\n")

# print("\n")
# for x in platform:
#     print(x)

print(calc_load(platform))