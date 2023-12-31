lines = []
with open('inaoc.txt') as file:
    for l in file:
        lines.append(l.strip().split())

def calc_diffs(row):
    new_row = []
    x=0
    while(x < len(row)-1):
        new_row.append(int(row[x+1])-int(row[x]))
        x = x +1
    return new_row
diffs = []
hist = []
for l in range(len(lines)+1):
    if(diffs != []):
        diffs.append(calc_diffs(diffs[-1]))
        rev = list(reversed(diffs))
        for x in range(len(diffs)):
            if(x == 0):
                rev[x].insert(0,0)
            else:
                a =  rev[x][0]
                b = rev[x-1][0]
                rev[x].insert(0,   a-b)
        hist.append(rev[-1][0])
    diffs = []
    if(l<len(lines)):
        lines[l] = [eval(i) for i in lines[l]]
        row = lines[l]
        diffs.append(row)
        len_cc = len(set(calc_diffs(row)))
        first_cc = list(set(calc_diffs(row)))[0]
        while not all(num == 0 for num in calc_diffs(row)):
            row = calc_diffs(row)
            diffs.append(row)
print(sum(hist))