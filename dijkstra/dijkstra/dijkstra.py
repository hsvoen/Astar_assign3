from heapq import heappush, heappop
import math
import itertools

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task.ID in entry_finder:
        remove_task(task.ID)


    count = next(counter)
    entry = [priority, count, task.ID, task]
    entry_finder[task.ID] = entry
    heappush(pq, entry)

def remove_task(ID):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(ID)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, ID, task = heappop(pq)
        if ID is not REMOVED:
            del entry_finder[ID]
            return task
    raise KeyError('pop from an empty priority queue')


def findStart(board):
	for x in range(len(board)):
		for y in range(len(board[x])):
			if board[x][y] == "A":
				return [x,y]

def findGoal(board):
	for x in range(len(board)):
		for y in range(len(board[x])):
			if board[x][y] == "B":
				return [x,y]

######################### Boardreading functions ############################
def readBoard(subprob, boardIndex):
	if(subprob >=1 and subprob <=4 and boardIndex >=1 and boardIndex <=4 ):
		f=open("board-%s-%s.txt" % (subprob, boardIndex),"r")
		board = f.read().splitlines()

		f.close()
		return board

	else:
		print("readBoard got invalid Parameters")

def writeBoard(solution, subprob, boardIndex):
	f=open("solution-%s-%s.txt" % (subprob, boardIndex),"w")
	f.write(solution)

	f.close()


def getWeight(string):
	if string == ".":
		return 1
	elif string == "#":
		return 999999999
	elif string == "w":
		return 100
	elif string == "m":
		return 50
	elif string == "f":
		return 10
	elif string == "g":
		return 5
	elif string == "r":
		return 1
	else:
		return 0

##############################################################3

	
class Vertex:						#Vertex class
	def __init__(self, id, pos, dist, prev):
		self.ID = id		
		self.pos = pos
		self.d = dist
		self.pre = prev
	def __lt__ (self,other):
		return self.d < other.d
	isClosed = False

def dijkstra(board, start, goal):				#Wrote dijkstra from scratch
	vertexBoard = []	
	row = [0]*len(board[0])
	for i in range(len(board)):
	 	vertexBoard.append(list(row))
		

	counter = 0						#creating all vertices and adding them to the priority que
	for i in range(len(board)):				
		for j in range(len(board[0])):
			if i == start[0] and j == start[1]:
				counter += 1
				vertexBoard[i][j] = Vertex(counter,[i,j],0,[-1,-1])
			else:
				counter += 1
				vertexBoard[i][j] = Vertex(counter, [i,j],9999999, [-1,-1])
			add_task(vertexBoard[i][j],vertexBoard[i][j].d)
	
#Iterates over vertices
	while len(entry_finder) > 0:			
		u = pop_task()
		x = u.pos[0]
		y = u.pos[1]
		if x == goal[0] and y == goal[1]:
			break	
#Update values for adjacent nonclosed vertices
		if (x-1 >= 0) and (vertexBoard[x-1][y].isClosed == False):
			alt = u.d + getWeight(board[x-1][y])
			if alt < vertexBoard[x-1][y].d:
				vertexBoard[x-1][y].d = alt
				vertexBoard[x-1][y].pre = [x,y]
				add_task(vertexBoard[x-1][y], alt)

		if (x+1 < len(board)) and (vertexBoard[x+1][y].isClosed == False):
			alt = u.d + getWeight(board[x+1][y])
			if alt < vertexBoard[x+1][y].d:
				vertexBoard[x+1][y].d = alt
				vertexBoard[x+1][y].pre = [x,y]
				add_task(vertexBoard[x+1][y], alt)

		if (y-1 >=0) and (vertexBoard[x][y-1].isClosed == False):
			alt = u.d + getWeight(board[u.pos[0]][u.pos[1]-1])
			if alt < vertexBoard[x][y-1].d:
				vertexBoard[x][y-1].d = alt
				vertexBoard[x][y-1].pre = [x,y]
				add_task(vertexBoard[x][y-1], alt) 

		if y+1 < len(board[0]) and vertexBoard[x][y+1].isClosed == False:
			alt = u.d + getWeight(board[x][y+1])
			if alt < vertexBoard[x][y+1].d:
				vertexBoard[x][y+1].d = alt
				vertexBoard[x][y+1].pre = [x,y]
				add_task(vertexBoard[x][y+1], alt)
#closing the vertex before progressing to the next one.
		vertexBoard[x][y].isClosed = True
#long time since i've coded in python, this is an overly complicated way of building a changeable replica of the board.
	solution = []
	vertexStatus = []	
	row = [0]*len(board[0])
	for i in range(len(board)):
	 	solution.append(list(row))
		vertexStatus.append(list(row))
	for i in range(len(board)):
		for j in range(len(board[0])):
			solution[i][j] = board[i][j]
			if vertexBoard[i][j].d < 9999999:
				if vertexBoard[i][j].isClosed == True:
					vertexStatus[i][j] = 'x'
				else:
					vertexStatus[i][j] = 'o'
			else:
				vertexStatus[i][j] = '.'	

#iterates backwards from the goal
	vertex = vertexBoard[goal[0]][goal[1]]
	totalDistance = str(vertex.d)
	while (vertex.pos[0] == start[0] and vertex.pos[1] == start[1]) == False:
		if board[vertex.pos[0]][vertex.pos[1]] == '.':
			solution[vertex.pos[0]][vertex.pos[1]] = 'o'
		else:
			solution[vertex.pos[0]][vertex.pos[1]] = board[vertex.pos[0]][vertex.pos[1]].capitalize()
		vertex = vertexBoard[vertex.pre[0]][vertex.pre[1]]
	finalmap = ""	
#converting to string	
	for row in solution:
		test = "".join(row) + "\n"
		finalmap += test
	print finalmap
	vertexStatus[start[0]][start[1]] = 'A'
	vertexStatus[goal[0]][goal[1]] = 'B'
	vertexData= ""
	for row in vertexStatus:
		test = "".join(row) + "\n"
		vertexData += test
	print vertexData
	return "map with most efficient path: %s \n \n"%totalDistance + finalmap + "\n \n \n map of open vertexes(O) and closed vertexes(X) \n " + vertexData + " \n "

for i in [1,2]:
	for k in [1,2,3,4]:
		print "\n\nSearching for the shortest pathboards\\board-%s-%s.txt" %(i, k)

		pq = []                         # list of entries arranged in a heap
		entry_finder = {}               # mapping of tasks to entries
		REMOVED = '<removed-task>'      # placeholder for a removed task
		counter = itertools.count()     # unique sequence count


		board = readBoard(i,k)
		writeBoard(dijkstra(board,findStart(board),findGoal(board)),i,k)
