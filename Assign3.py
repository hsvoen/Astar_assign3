
# link to other implementation
# http://code.activestate.com/recipes/577519-a-star-shortest-path-algorithm/

from heapq import heappush, heappop
import math

############### WARNING
# x and y are opposite of what is logical. [x][y] is correct for table lookup.





###############################Various functions implemented here######################3
#Reads the board from text files.
def readBoard(subprob, boardIndex):
	if(subprob >=1 and subprob <=4 and boardIndex >=1 and boardIndex <=4 ):
		f=open("boards\\board-%s-%s.txt" % (subprob, boardIndex),"r")
		board = f.read().splitlines()

		f.close()
		return board

	else:
		print("readBoard got invalid Parameters")



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
	else:
		return 0


def propogatePathImprovement(node):



	for childCord in node.children:
		childX = childCord[0]
		childY = childCord[1]
		child = tableOfNodes[childX][childY]

		#if n0.dist + n0.weight < tableOfNodes[dx][dy].dist  #tests if the node is a better parent than the old one
		if node.dist + child.weight < child.dist:
			child.dist = node.dist + child.weight
			child.updateTotalDist(goalX,goalY)
			child.setParent(node)

			tableOfNodes[childX][childY] = child

			propogatePathImprovement(tableOfNodes[childX][childY])


def print_solution(board, table_of_nodes, goalX, goalY):

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
		x = table_of_nodes[x][y].parentX
		y = table_of_nodes[x][y].parentY

	for x in range(len(board)):
		for y in range(len(board[x])):
			if solution[x][y] == 0:
				solution[x][y] = board[x][y]
	finalmap = ""
	for row in solution:
		test = "".join(row) +"\n"
		finalmap = finalmap + test

	return finalmap


########## Class start #############################
class Node:
	#state
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
	def __init__(self, xPos, yPos, distance, totalDist, weight):
		self.xPos = xPos
		self.yPos = yPos
		self.dist = distance
		self.totalDist = totalDist
		self.weight = weight

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





#Search states hash table?
# Or just have a list of nodes with ID? Have the Index be the ID?

#Best first search, A*

#Takes in a board and returns the shortest path from start to goal
def Astar(board):


	#Finding start and goal positions
	start_pos = findStart(board)
	startX = start_pos[0]
	startY = start_pos[1]
	goal_pos = findGoal(board)
	goalX = goal_pos[0]
	goalY = goal_pos[1]
	



	# #Generating open and closed nodes lists
	#closedNodes = []
	#openNodes = []
	tableOfNodes = [] #contains all nodes created.

	row = [0]*len(board[0])
	for i in range(len(board)):
	 	#closedNodes.append(list(row))
	 	#openNodes.append(list(row))
	 	tableOfNodes.append(list(row))



	#Priority queue/Open nodes
	priQue = [[], []]
	priInd = 0 #queue index

	# Creating the start node and pushing it into the list of open nodes.
	n0 = Node(startX, startY, 0, 0, 0)
	n0.updateTotalDist(goalX, goalY)
	n0.isOpen = True

	heappush(priQue[priInd],n0)
	

	#openNodes[startX][startY] = n0
	tableOfNodes[startX][startY] =n0
	


	#Possible directions to move in.
	directions = [[1,0], [-1,0], [0,1], [0,-1]]

	#Agenda loop
	#Will run while there are still elements int the priority queue.
	while len(priQue[priInd]) > 0:
		print "Agenda loop"


		n0 = heappop(priQue[priInd])
		x = n0.xPos
		y = n0.yPos
		
		print "popping node, x = %i, y = %i " %(x, y)
		print "node children:"
		print tableOfNodes[x][y].children

		tableOfNodes[x][y].isOpen = False

		#closedNodes[x][y] = n0 #replace with indices?
		#openNodes[x][y] = 0


		#If goal is reached, return and exit.
		if (x == goalX and y == goalY):

			print tableOfNodes[goalX][goalY].totalDist
			return print_solution(board, tableOfNodes, goalX, goalY)

			#Do stuff here.

			#return stuff

		#Expand childrens of the node.
		for direct in directions:
			dx = x + direct[0]
			dy = y + direct[1]

			print "Searching node dx = %i, dy = %i" %(dx, dy)
			print "checking in direction x = %i, y = %i" %(direct[0], direct[1])
			
			# Make sure that the move does not exit the board
			if(dx >= 0 and dy >= 0 and dy < len(board[0]) and dx < len(board)):
				
				if(tableOfNodes[dx][dy] == 0 ):
					print "New node, x = %i, y = %i " %(dx, dy)
					#Add child to parent.
					weight = getWeight(board[dx][dy])
					nChild = Node(dx,dy, n0.dist + weight, 0, weight)
					nChild.updateTotalDist(goalX,goalY)
					nChild.setParent(n0)

					nChild.isOpen = True
					tableOfNodes[dx][dy] = nChild

					heappush(priQue[priInd], nChild)


				# check if children have allready been created
				elif (tableOfNodes[dx][dy] != 0 ):
					print "node allready created, x = %i, y = %i " %(dx, dy)
					if n0.dist + n0.weight < tableOfNodes[dx][dy].dist: #tests if the node is a better parent than the old one
						print "Better parent found"
						tableOfNodes[dx][dy].dist = n0.dist + n0.weight
						tableOfNodes[dx][dy].updateTotalDist(goalX, goalY)
						tableOfNodes[dx][dy].setParent(n0)

						if(tableOfNodes[dx][dy].isOpen):
							print "node is in open"

							try:
								print "searching priority queue for x = %i, y = %i " %(dx, dy)
								print "old length of priority queue: %i" %(len(priQue[priInd]))
								print "priInd = %i" % priInd
								while not (priQue[priInd][0].xPos == dx and priQue[priInd][0].yPos == dy):
									
									print "in queue: x = %i, y = %i " %(priQue[priInd][0].xPos,priQue[priInd][0].yPos)

									heappush(priQue[1 - priInd], priQue[priInd][0])
									heappop(priQue[priInd])

								print "found node x = %i, y = %i " %(priQue[priInd][0].xPos,priQue[priInd][0].yPos)
								heappop(priQue[priInd]) # remove the target node
								# empty the larger size priority queue to the smaller one
								if len(priQue[priInd]) > len(priQue[1 - priInd]):
									priInd = 1 - priInd
									while len(priQue[priInd]) > 0:
										heappush(priQue[1-priInd], priQue[priInd][0])
										heappop(priQue[priInd])       
									priInd = 1 - priInd
									heappush(priQue[priInd], tableOfNodes[dx][dy]) # add the better node instead
								print "new length of priority queue: %i" %(len(priQue[priInd]))
							except:
								print "####################################exception happened##################################################"
								print "priority queue update failed for x = %i, y = %i " %(dx, dy)
							
						

						else:
							propogatePathImprovement(tableOfNodes[dx][dy])				






				
	


	# for rows in tableOfNodes:
	# 	for nodes in rows:
	# 		print nodes.totalDist
	print "Search failed"
	return None #search failed

		






#####Testcode here###########
board = readBoard(1,1)
print board[4][9]


print Astar(board)
