start = findstart(board)

class vertex:
	def __init__(pos, dist, prev):
		self.pos = pos
		self.d = dist
		self.pre = prev
	def __lt__ (self,other):
		return self.d < other.d


def dijkstra(board, start):
	vertexBoard = board
	Q = []
	for i in range(len(board)):
		for j in range(len(board[0])):
			if i == start[0] and j == start[1]:
				vertexBoard[i]][j] = vertex([i,j],0,[-1,-1])
			else:
				vertexBoard[i][j] = vertex([i,j],10*10^9, [-1,-1])
			heappush(Q, vertexBoard[i][j])
		
	while len(Q) > 0:
		u = heappop.Q()
		if u.pos[0]-1 >= 0:
			alt = u.d + value(board[u.pos[0]-1][u.pos[1]])
			if alt < vertexBoard[u.pos[0]-1][u.pos[1]].d:
				vertexBoard[u.pos[0]-1][u.pos[1]].d = alt
				vertexBoard[u.pos[0]-1][u.pos[1]].pre = [u.pos[0],u.pos[1]]
		if u.pos[0]+1 < len(board):
			alt = u.d + value(board[u.pos[0]+1][u.pos[1]])
			if alt < vertexBoard[u.pos[0]+1][u.pos[1]].d:
				vertexBoard[u.pos[0]+1][u.pos[1]].d = alt
				vertexBoard[u.pos[0]+1][u.pos[1]].pre = [u.pos[0],u.pos[1]]
		if u.pos[1]-1 >= 0:
			alt = u.d + value(board[u.pos[0]][u.pos[1]-1])
			if alt < vertexBoard[u.pos[0]][u.pos[1]-1].d:
				vertexBoard[u.pos[0]][u.pos[1]-1].d = alt
				vertexBoard[u.pos[0]][u.pos[1]-1].pre = [u.pos[0],u.pos[1]]
		if u.pos[1]+1 < len(board[0]):
			alt = u.d + value(board[u.pos[0]][u.pos[1]+1])
			if alt < vertexBoard[u.pos[0]][u.pos[1]+1].d:
				vertexBoard[u.pos[0]][u.pos[1]+1].d = alt
				vertexBoard[u.pos[0]][u.pos[1]+1].pre = [u.pos[0],u.pos[1]]
		
	#### returnerer distanser og følgere av vertexes. 
	distBoard = board
	prevBoard = board
	for i in range(len(board)):
		for j in range(len(board[0])):
			distBoard[i][j] = vertexBoard[i][j].d
			prevBoard[i][j] = vertexBoard[i][j].pre
	
	return distBoard, prevBoard
