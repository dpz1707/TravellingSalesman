import math

maxsize = float('inf')

def copyFinal(currentPath):
	finalPath[:N + 1] = currentPath[:]
	finalPath[N] = currentPath[0]


def firstMinimum(adjacencyMap, i):
	minimum = maxsize
	for k in range(N):
		if adjacencyMap[i][k] < minimum and i != k:
			minimum = adjacencyMap[i][k]

	return min


def secondMinimum(adjacencyMap, i):
	current, nex = maxsize, maxsize
	for j in range(N):
		if i == j:
			continue
		if adjacencyMap[i][j] >= current:
			nex = current
			current = adjacencyMap[i][j]

		elif(adjacencyMap[i][j] >= nex and adjacencyMap[i][j] != current):
			nex = adjacencyMap[i][j]

	return nex


def TSPRec(adjacencyMap, currentBound, currentWeight, level, currentPath, hit):
  global finalRes

  if (level == N):
		

	  if adjacencyMap[currentPath[level - 1]][currentPath[0]] != 0:
			

		  currentRes = currentWeight + adjacencyMap[currentPath[level - 1]]
		  if currentRes < finalRes:
			  copyFinal(currentPath)
			  finalRes = currentRes
	  return


  for i in range(N):
		
		  if (adjacencyMap[currentPath[level-1]][i] != 0 and	hit[i] == False):
		    temp = currentBound
		    currentWeight += adjacencyMap[currentPath[level - 1]][i]


		  if level == 1:
		  	currentBound -= ((firstMinimum(adjacencyMap, currentPath[level - 1]) + firstMinimum(adjacencyMap, i)) / 2)
		  else:
			  currentBound -= ((secondMinimum(adjacencyMap, currentPath[level - 1]) + firstMinimum(adjacencyMap, i)) / 2)


		  if currentBound + currentWeight < finalRes:
			  currentPath[level] = i
			  hit[i] = True
				

			  TSPRec(adjacencyMap, currentBound, currentWeight,	level + 1, currentPath, hit)


		  currentWeight -= adjacencyMap[currentPath[level - 1]][i]
		  currentBound = temp


		  hit = [False] * len(hit)
		  for j in range(level):
			  if currentPath[j] != -1:
				  hit[currentPath[j]] = True


def TSP(adjacencyMap):
	

	currentBound = 0
	currentPath = [-1] * (N + 1)
	hit = [False] * N

	for i in range(N):
		currentBound += (firstMinimum(adjacencyMap, i) +
					secondMinimum(adjacencyMap, i))

	currentBound = math.ceil(currentBound / 2)


	hit[0] = True
	currentPath[0] = 0


	TSPRec(adjacencyMap, currentBound, 0, 1, currentPath, hit)


adjacencyMap = [[5, 10, 22, 26],
	[10, 5, 35, 25],
	[22, 35, 5, 34],
	[26, 25, 34, 5]]
N = 4


finalPath = [None] * (N + 1)


hit = [False] * N


finalRes = maxsize

TSP(adjacencyMap)

print("Cost:", finalRes)
print("Path: ")
for i in range(N + 1):
	print(finalPath[i], end = ' ')



