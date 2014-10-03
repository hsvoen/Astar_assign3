

import Queue
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

#writes a string to a .txt file
def writeBoard(solution, subprob, boardIndex):
	f=open("BFSsolutions\\board-%s-%s.txt" % (subprob, boardIndex),"w")
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

#returns an integer with the weight of a given string.
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


def propogatePathImprovement(node, tableOfNodes, goalX, goalY):

	for childCord in node.children:
		childX = childCord[0]
		childY = childCord[1]
		child = tableOfNodes[childX][childY]

		if child != 0 and node.dist + tableOfNodes[childX][childY].weight < child.dist:

			tableOfNodes[childX][childY].dist = node.dist + child.weight
			tableOfNodes[childX][childY].updateTotalDist(goalX,goalY)
			tableOfNodes[childX][childY].setParent(node)
			propogatePathImprovement(tableOfNodes[childX][childY], tableOfNodes, goalX, goalY)







# Prints the shortest path and all closed and open nodes to the console as a string, and returns a string containing both.
def print_solution(board, table_of_nodes, goalX, goalY):
	print "Printing solution to console"
	x = goalX
	y = goalY

	solution = []
	openOrClosed = []
	row = [0]*len(board[0])
	for i in range(len(board)):
	 	solution.append(list(row))
	 	openOrClosed.append(list(row))

	#starting from the goal, iterate through the best parents of each node until the start is reached.
	while board[x][y] != 'A':
		if board[x][y] == '.':
			solution[x][y] = 'o'
		else:
			solution[x][y] = board[x][y].capitalize()
		next_x = table_of_nodes[x][y].parentX
		next_y = table_of_nodes[x][y].parentY
		x = next_x
		y = next_y

	#Creates the open and closed nodes string
	for x in range(len(board)):
		for y in range(len(board[x])):
			if(board[x][y]== "A"):
				openOrClosed[x][y] = "A"
			elif(board[x][y]== "B"):
				openOrClosed[x][y] = "B"
			elif(table_of_nodes[x][y] == 0):
				if(board[x][y]== "#"):
					openOrClosed[x][y] = "#"
				else:
					openOrClosed[x][y] = "."
			elif(table_of_nodes[x][y].isOpen):
				openOrClosed[x][y] = "O"
			elif (not table_of_nodes[x][y].isOpen):
				openOrClosed[x][y] = "X"

			if solution[x][y] == 0:
				solution[x][y] = board[x][y]
	
	#Combines the lists into strings
	finalmap = ""
	for row in solution:
		test = "".join(row) +"\n"
		finalmap = finalmap + test
	finalmap = finalmap + "\n\nTotal distance/weight from start to destination is %i" %table_of_nodes[goalX][goalY].totalDist
	print finalmap

	finalOC = ""
	for row in openOrClosed:
		test = "".join(row) +"\n"
		finalOC = finalOC + test
	finalOC = finalOC
	print finalOC

	return "shortest path found with the BFS algorithm:\n\n" +finalmap + "\n\n\n\nVisualisation of open and closed nodes\n" + finalOC +"\n\nOpen nodes = O, closed nodes = X, unexplored nodes = ., inaccsessible nodes = # "




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
	parentX = 0 #indices for current best parent
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
		self.children = []



	def addChild(self, other): 			
		self.children.append([other.xPos, other.yPos])

	#takes the manhatten distance to the goal
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
	q = Queue.Queue(maxsize=0) #The FIFO queue for storing open nodes
	
	tableOfNodes = [] 				# contains all nodes created.
	row = [0]*len(board[0])
	for i in range(len(board)):
	 	tableOfNodes.append(list(row))
	nodeID = 1 #Sets the unique node ID

	# Creating the start node and pushing it into the list of open nodes.
	n0 = Node(startX, startY, 0, 0, 0, nodeID)
	nodeID += 1
	n0.updateTotalDist(goalX, goalY)
	n0.isOpen = True

	q.put(n0)
	tableOfNodes[startX][startY] =n0
	


	#Possible directions to move in.
	directions = [[1,0], [-1,0], [0,1], [0,-1]]

	#Agenda loop
	#Will run while there are still elements int the priority queue.
	while not(q.empty()) :
		
		n0 = q.get()
		x = n0.xPos
		y = n0.yPos

		tableOfNodes[x][y].isOpen = False

		#If goal is reached, return and exit.
		if (x == goalX and y == goalY):

			print "Goal found. Total distance is: %i" %n0.totalDist
			return print_solution(board, tableOfNodes, goalX, goalY)


		#Expand childrens of the node.
		for direct in directions:
			dx = x + direct[0]
			dy = y + direct[1]

			# Make sure that the move does not exit the board
			if(dx >= 0 and dy >= 0 and dy < len(board[0]) and dx < len(board)):

				if(tableOfNodes[dx][dy] == 0 ):
					
					#Checks that the child is not a closed node before opening it
					if (board[dx][dy] != "#"):

						#Initialising the node, pushing it into the queue of open nodes.
						weight = getWeight(board[dx][dy])
						nChild = Node(dx,dy, n0.dist + weight, 0, weight, nodeID)
						nodeID += 1
						nChild.updateTotalDist(goalX,goalY)
						nChild.setParent(n0)

						nChild.isOpen = True

						tableOfNodes[dx][dy] = nChild
						tableOfNodes[x][y].children.append([dx,dy])
						q.put(tableOfNodes[dx][dy])

				# check if children have allready been created
				elif (tableOfNodes[dx][dy] != 0 ):

					if tableOfNodes[x][y].dist + tableOfNodes[dx][dy].weight < tableOfNodes[dx][dy].dist: #tests if the node is a better parent than the old one
						
						tableOfNodes[dx][dy].dist = tableOfNodes[x][y].dist + tableOfNodes[dx][dy].weight
						tableOfNodes[dx][dy].updateTotalDist(goalX, goalY)
						tableOfNodes[dx][dy].setParent(tableOfNodes[x][y])

						if not (tableOfNodes[dx][dy].isOpen):
							propogatePathImprovement(tableOfNodes[dx][dy], tableOfNodes, goalX, goalY)				

	print "Search failed"
	return None #search failed

		










#Main()
for i in [1,2]:
	for k in [1,2,3,4]:

		print "======================================================\n\nSearching for the shortest pathboards\\board-%s-%s.txt \n\n=======================================0" %(i, k)

		board = readBoard(i,k)

		writeBoard(Astar(board), i, k)
