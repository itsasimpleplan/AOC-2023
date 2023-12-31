order = ["J","1", "2", "3", "4", "5", "6", "7", "8", "9", "T" , "Q", "K", "A"]
hands = {}
with open('inputaoc.txt') as file:
    score = []
    for hand in file:
        cards = hand.split()[0]
        bet = hand.split()[1]
        hands[cards] = bet
        counts = {}
        for i in range(len(cards)):
            counts[cards[i]] = 1
            for j in range(len(cards)):
                if(i != j):
                    if(cards[i] == cards[j]):
                        if(cards[i] in counts):
                            count = counts[cards[i]]+1
                            nc = {cards[i]:count}
                            counts.update(nc)
                        else:
                            counts[cards[i]] = 1
            
        sort_counts = sorted(counts.items(), key=lambda x:x[1], reverse=True)
        sort_counts = dict(sort_counts)
        parsed = False
        if("J" in sort_counts):
            print(sort_counts)
            add = sort_counts["J"]
            max_card = max(sort_counts, key=sort_counts.get)
            sort_counts[max_card] =  sort_counts[max_card] + add
            sort_counts["J"] = 1
        print(sort_counts)
        print("\n")
        for c in sort_counts:
            if not parsed and sort_counts[c] == 5:
                score.append(("7"+cards,bet))
                parsed = True
                break
            if not parsed and sort_counts[c] == 4:
                score.append(("6"+cards,bet))
                parsed = True
                break
            if not parsed and sort_counts[c] == 3:
                for o in sort_counts:
                    if(c != o):
                        if(sort_counts[o] == 2):
                            score.append(("5"+cards,bet))
                            parsed = True
                            break
                if not parsed:
                    score.append(("4"+cards,bet))
                    parsed = True
                    break
            if not parsed and sort_counts[c] == 2:
                for o in sort_counts:
                    if(c != o):
                        if(sort_counts[o] == 2):
                            score.append(("3"+cards,bet))
                            parsed = True
                            break
                if not parsed:
                    score.append(("2"+cards,bet))
                    parsed = True
                    break
            if not parsed and sort_counts[c] == 1:
                score.append(("1"+cards,bet))
                parsed = True
                        
# sort_score = sorted(score.items(), key=lambda x:x[1], reverse=True)
# sort_score = dict(sort_score)
# fives = []
# fours = []
# threes = []
# twos = []
# ones = []
# zeros = []
# for key in sort_score:
#     if(sort_score[key] == 5):
#         fives.append(key[0])
#     if(sort_score[key] == 4):
#         fours.append(key[0])
#     if(sort_score[key] == 3):
#         threes.append(key[0])
#     if(sort_score[key] == 2):
#         twos.append(key[0])
#     if(sort_score[key] == 1):
#         ones.append(key[0])
#     if(sort_score[key] == 0):
#         zeros.append(key[0])

def cmp_items(a, b):
    if order.index(a) > order.index(b):
        return 1
    elif a == b:
        return 0
    else:
        return -1


def sort_list(list):
    sorted = []
    if(sorted == []):
        sorted.append(list[0])
    for j in list:
        parsed = False
        for i in sorted:
            if(j == i or j in sorted):
                break
            else:
               for k in range(len(j[0])):
                    itm_list = j[0][k]
                    itm_sort = i[0][k]
                    if(cmp_items(itm_list, itm_sort)) == 1:  
                        idx = sorted.index(i)
                        sorted.insert(idx, j)
                        break
                    if(cmp_items(itm_list, itm_sort)) == -1:  
                        break
        if(j not in sorted):
            sorted.append(j)
    return sorted
print(score)       
ranked = sort_list(score)
print(ranked)
high = len(ranked)

sum = 0
for i in ranked:
    sum = sum + int(int(i[1])*high)
    high = high -1
print(sum)

# def sort_list(list):
#     sorted = []
#     print(list)
#     for j in range(len(list)-1):
#         for i in range(len(list[0])):
#             if(cmp_items(list[j][0][i], list[j+1][0][i])) == 1:
#                 if(list[j+1] in sorted):
#                     idx = sorted.index(list[j+1])
#                     sorted.insert(idx, list[j])
#                     break
#                 elif(list[j] in sorted):
#                     idx = sorted.index(list[j])
#                     sorted.insert(idx+1, list[j+1])
#                     break
#                 else:
#                     sorted.append(list[j])
#                     sorted.append(list[j+1])
#             if(cmp_items(list[j][0][i], list[j+1][0][i])) == -1:
#                 if(list[j] in sorted):
#                     idx = sorted.index(list[j])
#                     sorted.insert(idx, list[j+1])
#                     break
#                 elif(list[j+1] in sorted):
#                     idx = sorted.index(list[j+1])
#                     sorted.insert(idx+1, list[j])
#                 else:
#                     sorted.append(list[j+1])
#                     sorted.append(list[j])
#                     break
#     return(sorted)
           





# idx = 0
# high = len(sort_score)
# mult_bet = []
# rank = []
# for c in sort_score:
#     inBet = False
#     for l in rank:
#             if c[0] == l[0]:
#                 inBet= True
#     if(not inBet):
#         idx = idx+1
#         i = 0
#         sim = False
#         for o in sort_score:
#             i = i+1
#             for l in rank:
#                 if o[0] == l[0]:
#                     inBet= True
#             if(i != idx and not inBet):
#                 if(sort_score[c] == sort_score[o]):
#                     for a in range(len(c[0])):
#                         first_hand = order.index(c[0][a])
#                         second_hand = order.index(o[0][a])
#                         if first_hand < second_hand:
#                             rank.append(o)
#                             rank.append(c)
#                             break
#                         if first_hand > second_hand:
#                             rank.append(c)
#                             rank.append(o)
#                             break
#                     sim = True
#                     break
#         if(not sim):
#             rank.append(c)
# #print((mult_bet))
# sum = 0
# for x in mult_bet:
#     sum = sum+x[1]

# print(rank)

            