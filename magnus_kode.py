def print_solution(board, table_of_nodes, goalX, goalY):
    x = goalX
    y = goalY
    while board[x][y] != A:
		if board[x][y] == '.':
			board[x][y] = 'o'
		else:
			board[x][y] = board[x][y].uppercase()
        x_next = table_of_nodes[x][y].best_parent_x
        y_next = table_of_nodes[x][y].best_parent_y
        x = x_next, y = y_next
    return board 

class Node:
    #state
    xPos        = 0
    yPos        = 0
    dist        = 0     #g - cost of getting to node
    estDist     = 0     #h - estimate cost to goal
    totalDist   = 0     #f-estimated total cost of solution path going through this node, f = g+h
	
	#går ut ifra at dette blir state
	##############################
    children = []
    def add_child(self, other):
        self.children.append(other)
	
    bestParentX = 0
    bestParentY = 0
	#####################################
	
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

#value funksjon. nødvendig?
def value(char):
	if char == '.' or char == 'r':
		return 1
	else if char == 'w':
		return 100
		#.... osv
		
		
if openNodes.empty():
	return FAIL
node = openNodes.pop() #gitt at open node er en heap med minste øverst
closed.push(node)
if node.xPos == goalX and node.yPos == goalY:
	return print_solution(Board, Table_of_nodes, goalX, goalY)
for alle retninger:
	if table_of_nodes[x][y] != 0:
		node.add_child(table_of_nodes[x][y])
		if node.g+value(board[x][y] < table_of_nodes[x][y].g:
			table_of_nodes[x][y].g = node.g+ value(board[x][y])
			table_of_nodes[x][y].bestParentX = node.Xpos
			table_of_nodes[x][y].bestParentY = node.Ypos
			table_of_nodes[x][y].updateTotal
	else if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
	else if == 0:
		table_of_nodes[x][y] = Node(x,y, node.g + value(board[x][y]), 0)
		table_of_nodes[x][y].updateTotalDist
		table_of_nodes[x][y].bestParentX = node.Xpos
		table_of_nodes[x][y].bestParentY = node.Ypos
		node.addChild(table_of_nodes[x][y])
		openNodes.append(child)
	
	
	
