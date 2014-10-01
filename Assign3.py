
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



########## Class start #############################
class Node:
	#state
	xPos 		= 0
	yPos 		= 0
	dist 		= 0 	#g - cost of getting to node
	estDist 	= 0		#h - estimate cost to goal
	totalDist 	= 0		#f-estimated total cost of solution path going through this node, f = g+h

	#parent - coordinates to the cheapest parent node?


	####Function declarations###
	def __init__(self, xPos, yPos, distance, totalDist):
		self.xPos = xPos
		self.yPos = yPos
		self.dist = distance
		self.totalDist = totalDist

	def __lt__(self, other): # Comparison method for the priority queue
		return self.totalDist < other.totalDist


	def estimate(self, xDest, yDest):
		xd = xDest - self.xPos
		yd = yDest - self.yPos

		#Takes manhattan distance
		d = abs(xd) + abs(yd)

		self.estDist = d

		return d

	def updateTotalDist(self, xDest, yDest):
		self.totalDist = self.estimate(xDest, yDest) + self.dist


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
	



	#Generating open and closed nodes lists
	closedNodes = []
	openNodes = []

	row = [0]*len(board[0])
	for i in range(len(board)):
		closedNodes.append(list(row))
		openNodes.append(list(row))

	print closedNodes


	#Priority queue
	priQue = [[], []]
	priInd = 0 #queue index

	# Creating the start node and pushing it into the list of open nodes.
	n0 = Node(startX, startY, 0, 0)
	n0.updateTotalDist(goalX, goalY)
	heappush(priQue[priInd],n0)
	openNodes[startX][startY] = n0.totalDist



	#Agenda loop
	#Will run while there are still elements int the priority queue.
	while len(priQue[priInd]) > 0:
		

		n0 = heappop(priQue[priInd])
		x = n0.xPos
		y = n0.yPos
		openNodes[x][y] = 0
		closedNodes[x][y] = 1


		#If goal is reached, return and exit.
		#if (x == goalX and y == goalY):
			#Do stuff here.

			#return stuff

		#Expand childrens of the node.

		# Generate directions

		direction = [[1,0],[1,],]


		






#####Testcode here###########
board = readBoard(1,1)
print board

Astar(board)
