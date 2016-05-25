import math
import copy


def isPerfectSquare(n):
    return int(math.sqrt(n))**2 == n


def returnFirstDigits(n):
    return n/100


def returnLastDigits(n):
    return n % 100

def areCyclic(n,m):
    return returnLastDigits(n) == returnFirstDigits(m)



# def findSolutions(canidate,total):
#     #print canidate[1]
#     results = copy.deepcopy(canidate)
#     ans = copy.deepcopy(results)
#     for target in total:
#         #print results
#         print target[0]
#         if areCyclic(canidate[-1],target[0]):
#             if target[0] == canidate:
#                 continue
#             if target[0] in results:
#                 continue
#             print "target",target[0]
#             results.append(target[0])
#             if len(results) == 6:
#                 ans.append(canidate)
#                 return ans
#             return ans.append(findSolutions(results,total))

#     return ans
def findSolutions(acc,total):
    if len(acc) == 6:
        #print acc
        if areCyclic(acc[-1][0],acc[0][0]):
            return acc
        else:
            return []
    numbers = []
    figure = []
    for item in acc:
        numbers.append(item[0])
        figure.append(item[1])

    newCanidates = []
    for target in total:
        if areCyclic(numbers[-1],target[0]):
            if target[0] == numbers[-1]:
                continue
            if target[0] in numbers:
                continue
            if target[1] in figure:
                continue
            newCanidates.append(target)
    #print newCanidates
    if newCanidates == []:
        return []

    l = []

    for newCanidate in newCanidates:
        l.append(findSolutions(acc + [newCanidate],total))
    #l nog ff filteren
    # for sol in l:
    #     print sol
    #     if areCyclic(sol[-1][0],sol[0][0]):
    #         res.append(sol)
    return l

def main():
    canidates = []
    for i in range(1000, 10000):
        mark = []
        if (-1 + math.sqrt(1 + 8*i))%2==0:
            # Triangle
            mark.append(3)
        if isPerfectSquare(i):
            # Square
            mark.append(4)
        if (1+ math.sqrt(1 + 24*i))%6 ==0:
            # Penta
            mark.append(5)
        if (1+math.sqrt(1+8*i)) % 4 == 0:
            # Hexa
            mark.append(6)
        if (3+math.sqrt(9 + 40*i))%10==0:
            # Hepta
            mark.append(7)
        if (2+math.sqrt(4+12*i)) % 6 == 0:
            # Octa
            mark.append(8)
        if mark == []:
            continue
        for mk in mark:
            canidates.append((i,mk))

    total = copy.deepcopy(canidates)
    #print total
    results=[]
    #integers = []
    for canidate in canidates:
    #    integers.append(canidate[0])
        if findSolutions([canidate],total) == []:
            continue
        results.append (findSolutions([canidate],total))
    #print results
    for res in results:
        print res
        print "next"
    # print findSolutions([(8128,3)],total)
    #print integers
    #print results


main()






# [(2512, 7), (1281, 8), (8128, 6), (2882, 5), (8256, 3), (5625, 4)
# n    32    



# (1281, 8), (8128, 6), (2882, 5), (8256, 3), (5625, 4), (2512, 7)
# n                                                          32

# (2882, 5), (8256, 3), (5625, 4), (2512, 7), (1281, 8), (8128, 6)

# (8128, 6), (2882, 5), (8256, 3), (5625, 4), (2512, 7), (1281, 8)

# (8256, 3), (5625, 4), (2512, 7), (1281, 8), (8128, 6), (2882, 5)

# (5625, 4), (2512, 7), (1281, 8), (8128, 6), (2882, 5), (8256, 3)

# def findSolutions(acc,total):
#     if len(acc) == 6:
#         print acc
#         return acc

#     newCanidates = []
#     for target in total:
#         if areCyclic(acc[-1],target[0]):
#             if target[0] == acc[-1]:
#                 continue
#             if target[0] in acc:
#                 continue
#             newCanidates.append(target[0])
#     #print newCanidates
#     l = []
#     for newCanidate in newCanidates:
#         l.append(findSolutions(acc + [newCanidate],total))

#     #l nog ff filteren
#     return l