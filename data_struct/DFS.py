# -*- coding: utf-8 -*-
# @Author: Teiei
# @Date:   2018-08-18 15:29:23
# @Last Modified by:   Teiei
# @Last Modified time: 2018-08-18 18:47:40

from Graph import Graph


def DFS(G, v):
	'''[summary] deep first trave for a Graph

	[description]

	Arguments:
		G {[Graph]} -- [图的数据结构]
		v {[int]} -- [起始节点]
	'''
	G.set_mark_visited(v)
	print(v)
	t = G.first(v)
	while(t != -1):
		if(G.mark[t] == "UNVISITED"):
			DFS(G,t)
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
	DFS(G,0)
