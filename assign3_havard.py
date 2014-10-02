
# link to other implementation
# http://code.activestate.com/recipes/577519-a-star-shortest-path-algorithm/

from heapq import heappush, heappop
import math
import itertools



############### WARNING
# x and y are opposite of what is logical. [x][y] is correct for table lookup.







###############################Various functions implemented here######################

#Reads the board from text files.
def readBoard(subprob, boardIndex):
	if(subprob >=1 and subprob <=4 and boardIndex >=1 and boardIndex <=4 ):
		f=open("boards\\board-%s-%s.txt" % (subprob, boardIndex),"r")
		board = f.read().splitlines()

		f.close()
		return board

	else:
		print("readBoard got invalid Parameters")

def writeBoard(solution, subprob, boardIndex):
	f=open("solutions\\board-%s-%s.txt" % (subprob, boardIndex),"w")
	f.write(solution)

	f.close()


# returns list with indices of the start coordinate
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

def getWeight(string):

	#for subproblem A.1
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


def propogatePathImprovement(node):
	print "propgate path improvement is run"
	for childCord in node.children:
		childX = childCord[0]
		childY = childCord[1]
		child = tableOfNodes[childX][childY]

		if node.dist + child.weight < child.dist:
			child.dist = node.dist + child.weight
			child.updateTotalDist(goalX,goalY)
			child.setParent(node)

			tableOfNodes[childX][childY] = child

			if child.isOpen:
				add_task(child,child.totalDist)

			propogatePathImprovement(tableOfNodes[childX][childY])








def print_solution(board, table_of_nodes, goalX, goalY):
	print "Printing solution to console"
	x = goalX
	y = goalY

	solution = []
	row = [0]*len(board[0])
	for i in range(len(board)):
	 	solution.append(list(row))



	while board[x][y] != 'A':
		
		if board[x][y] == '.':
			solution[x][y] = 'o'
		else:
			solution[x][y] = board[x][y].capitalize()
		print "x = %i, y = %i, symbol: %s" %(x, y, solution[x][y])
		next_x = table_of_nodes[x][y].parentX
		next_y = table_of_nodes[x][y].parentY
		x = next_x
		y = next_y
	for x in range(len(board)):
		for y in range(len(board[x])):
			if solution[x][y] == 0:
				solution[x][y] = board[x][y]
	finalmap = ""
	for row in solution:
		test = "".join(row) +"\n"
		finalmap = finalmap + test

	return finalmap


######################## Priority queue implemented here #############################################



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








########## Class start #############################
class Node:
	#state
	ID 			= 0
	xPos 		= 0
	yPos 		= 0
	dist 		= 0 	#g - cost of getting to node
	estDist 	= 0		#h - estimate cost to goal
	totalDist 	= 0		#f-estimated total cost of solution path going through this node, f = g+h

	#parents and children
	children = [] #Stores the indices of the child [x,y], use it to look up in the tableOfNodes
	parentX = 0 #coordinates for current best parent
	parentY = 0

	weight = 0 
	isOpen = False #use this variable to decide if the node is in the open or closed list?

	####Function declarations###
	def __init__(self, xPos, yPos, distance, totalDist, weight, ID):
		self.xPos = xPos
		self.yPos = yPos
		self.dist = distance
		self.totalDist = totalDist
		self.weight = weight
		self.ID = ID

	def __lt__(self, other): # Comparison method for the priority queue
		return self.totalDist < other.totalDist

	def addChild(self, other):
		children.append([other.xPos, other.Ypos])

	def estimate(self, xDest, yDest):
		xd = xDest - self.xPos
		yd = yDest - self.yPos

		#Takes manhattan distance
		d = abs(xd) + abs(yd)

		self.estDist = d

		return d

	def updateTotalDist(self, xDest, yDest):
		self.totalDist = self.estimate(xDest, yDest) + self.dist

	def setParent(self, parent):
		self.parentX = parent.xPos
		self.parentY = parent.yPos

	# status: open/closed
	# parent: pointer to current best (cheapest) parent node
	# kids: list of all successor nodes.

##################class end#####################


















#A* algorithm
#Takes in a board and returns the shortest path from start to goal
def Astar(board):


	#Finding start and goal positions
	start_pos = findStart(board)
	startX = start_pos[0]
	startY = start_pos[1]
	goal_pos = findGoal(board)
	goalX = goal_pos[0]
	goalY = goal_pos[1]
	
	#Priority queue/Open nodes
	#pq = []                         # list of entries arranged in a heap
	#entry_finder = {}               # mapping of tasks to entries
	#REMOVED = '<removed-task>'      # placeholder for a removed task
	#counter = itertools.count()     # unique sequence count


	tableOfNodes = [] 				# contains all nodes created.

	row = [0]*len(board[0])
	for i in range(len(board)):
	 	tableOfNodes.append(list(row))

	nodeID = 1








	# Creating the start node and pushing it into the list of open nodes.
	n0 = Node(startX, startY, 0, 0, 0, nodeID)
	nodeID += 1
	n0.updateTotalDist(goalX, goalY)
	n0.isOpen = True

	#heappush(priQue[priInd],n0)
	add_task(n0, n0.totalDist)

	#openNodes[startX][startY] = n0
	tableOfNodes[startX][startY] =n0
	


	#Possible directions to move in.
	directions = [[1,0], [-1,0], [0,1], [0,-1]]

	#Agenda loop
	#Will run while there are still elements int the priority queue.
	while len(entry_finder) > 0:
		print "Agenda loop"


		#n0 = heappop(priQue[priInd])
		n0 = pop_task()
		x = n0.xPos
		y = n0.yPos
		
		print "popping node, x = %i, y = %i " %(x, y)

		tableOfNodes[x][y].isOpen = False

		#closedNodes[x][y] = n0 #replace with indices?
		#openNodes[x][y] = 0


		#If goal is reached, return and exit.
		if (x == goalX and y == goalY):

			print "Goal found. Total distance is: %i" %n0.totalDist

			print tableOfNodes[goalX][goalY].totalDist
			return print_solution(board, tableOfNodes, goalX, goalY)


		#Expand childrens of the node.
		for direct in directions:
			dx = x + direct[0]
			dy = y + direct[1]

			#print "Searching node dx = %i, dy = %i, symbol: %s" %(dx, dy, board[dx][dy])
			print "checking in direction x = %i, y = %i" %(direct[0], direct[1])
			
			# Make sure that the move does not exit the board
			if(dx >= 0 and dy >= 0 and dy < len(board[0]) and dx < len(board)):
				
				if(tableOfNodes[dx][dy] == 0 ):
					print "New node, x = %i, y = %i " %(dx, dy)
					#Add child to parent.
					weight = getWeight(board[dx][dy])
					nChild = Node(dx,dy, n0.dist + weight, 0, weight, nodeID)
					nodeID += 1
					nChild.updateTotalDist(goalX,goalY)
					nChild.setParent(n0)

					nChild.isOpen = True
					tableOfNodes[dx][dy] = nChild

					add_task(nChild, nChild.totalDist)


				# check if children have allready been created
				elif (tableOfNodes[dx][dy] != 0 ):
					print "node allready created, x = %i, y = %i " %(dx, dy)
					if n0.dist + tableOfNodes[dx][dy].weight < tableOfNodes[dx][dy].dist: #tests if the node is a better parent than the old one
						print "Better parent found. Symbol: %s" %board[dx][dy]
						print "old distance: %i, new distance: %i" %(tableOfNodes[dx][dy].dist, n0.dist + n0.weight)
						
						tableOfNodes[dx][dy].dist = n0.dist + n0.weight
						tableOfNodes[dx][dy].updateTotalDist(goalX, goalY)
						tableOfNodes[dx][dy].setParent(n0)

						if(tableOfNodes[dx][dy].isOpen):
							print "node is in open"

							print "searching priority queue for x = %i, y = %i " %(dx, dy)

							add_task(tableOfNodes[dx][dy],tableOfNodes[dx][dy].totalDist) #For some reason, including this line breaks the program.							
						

						else:
							propogatePathImprovement(tableOfNodes[dx][dy])				

	print "Search failed"
	return None #search failed

		










#####Testcode here###########
for i in [1,2]:
	for k in [1,2,3,4]:
		print i, k

		pq = []                         # list of entries arranged in a heap
		entry_finder = {}               # mapping of tasks to entries
		REMOVED = '<removed-task>'      # placeholder for a removed task
		counter = itertools.count()     # unique sequence count


		board = readBoard(i,k)

		writeBoard(Astar(board), i, k)
