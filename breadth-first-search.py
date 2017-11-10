G = {'s':('p','q','u'),'p':('s','x','u'),'q':('s','w','x','y'),'t':('w','y'),'x':('w','p','q','y'),'u':('p','s','w'),'w':('u','x','q','t'),'y':('q','x','t')}

def breadthFirstSearch(graph, start):
	'''Iterates through the contents of a graph, and uses the breadth-first search algorithm explained in MAST20018 lectures where it scans all
	the other nodes in the order that they are closest to them. Does not compute distance.'''
	queue = [start]
	checked = {start}
	while queue:
		print("&=\\{"+",".join(queue)+"\\}\\\\")
		queue += [i for i in list(graph[queue.pop(0)]) if i not in checked]
		checked = set(list(checked)+queue)
	print("&=\\{}\\\\")

breadthFirstSearch(G, 's')
