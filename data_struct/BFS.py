# -*- coding: utf-8 -*-
# @Author: Teiei
# @Date:   2018-08-18 17:41:46
# @Last Modified by:   Teiei
# @Last Modified time: 2018-08-18 18:47:42
from Graph import Graph
def BFS(G,start):
	'''[summary] 图的宽度优先遍历
	
	[description]
	
	Arguments:
		G {[class Graph ]} -- [要遍历的图]
		start {[int]} -- [起始节点]
	''' 
	queue = []
	queue.append(start)
	G.set_mark_visited(start)
	while(len(queue) != 0):
		# dequeue
		v = queue[0]
		print(v)
		queue = queue[1:]
		t = G.first(v)
		while(t != -1):
			if(G.mark[t] == "UNVISITED"):
				G.set_mark_visited(t)
				queue.append(t)
			t = G.next(v,t)
if __name__ == '__main__':
	G = Graph(5)
	G.set_edge(0, 1, 1)
	G.set_edge(0, 4, 1)
	G.set_edge(1, 3, 1)
	G.set_edge(2, 4, 1)
	G.set_edge(3, 2, 1)
	G.set_edge(4, 1, 1)
	G.print_graph()
	BFS(G,0)
