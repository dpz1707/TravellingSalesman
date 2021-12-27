from sys import maxsize
from itertools import permutations

V = 4
 
def TSP(gLocation, s):
 
    vertices = []
    for i in range(V):
        if (i!=s):
            vertices.append(i)
 
    # minimum cost 
    minimum = maxsize
    nextPerm=permutations(vertices)
    for i in nextPerm:
 
        # current path cost
        currentCost = 0
 
        # calculating the current cost
        l = s
        for j in i:
            currentCost += gLocation[l][j]
            l = j
        currentCost += gLocation[l][s]
 
        # update the minimum
        minimum = min(minimum, currentCost)
         
    return minimum
 
 
gLocation = [[5, 17, 15, 20], [17, 5, 35, 25],
        [15, 35, 5, 30], [20, 25, 30, 5]]
s = 0
print(TSP(gLocation, s))

