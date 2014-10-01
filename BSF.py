class Vertex:
	def __init__(position, distance):
		self.pos = position
		self.dist = distance
	def __lt__(self, other):
		return self.dist < other.dist

start = findStart(board)

def BreadthFirstSearch(Board, start):
	Queue = []
	V = []
	v = Vertex(start, 0)
	V.push(v)
	Queue.append(v)
	while len(Queue) > 0:
		current = Queue.pop()
		if Board[current.pos] == 'B'
			return 

		