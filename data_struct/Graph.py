# -*- coding: utf-8 -*-
# @Author: Teiei
# @Date:   2018-08-18 10:22:12
# @Last Modified by:   Teiei
# @Last Modified time: 2018-08-18 11:30:42

'''
图的数据结构（邻接矩阵）
'''
class Graph(object):
	"""docstring for Graph"""
	# numVertex :int , the num of Vertex
	# numEdge	:int , the num of Edge 
	# matrix	:int** ,邻接矩阵表示的图	[[],[],[]]
	# mark 		:int list , is visted ?
	def __init__(self, numVertex):
		self.matrix = []
		self.mark = []
		for i in range(numVertex):
			self.matrix.append( [0 for j in range(numVertex)])
			self.mark.append( "UNVISTED")
		self.numVertex = numVertex
		self.numEdge = 0
	# v1:  int , source Vertex
	# v2:  int , target Vertex
	# wgt: the weigth of Edge (v1->v2)
	def set_edge(self,v1,v2,wgt):
		assert wgt > 0,"set_edge:weigth must >0"
		if self.matrix[v1][v2] == 0:
			self.matrix[v1][v2] =  wgt
			self.numEdge += 1
	def get_edge(self,v1,v2):
		return self.matrix[v1][v2]
	def get_V_nums():
		return self.numVertex
	def get_E_nums():
		return self.numEdge
	'''
	brief : return the first neigbor of v
	note: return -1 if no vertex connected to v
	'''
	def first(self,v):
		for i in range(self.numVertex):
			if(self.matrix[v][i] != 0):
				return i 
		return -1
	'''
	brief : get v1's neighbor after v2
	note: return -1 if no neighbor
	'''
	def next(self,v1,v2):
		for i in range(v2+1,self.numVertex):
			if self.matrix[v1][i] != 0:
				return i 
		return -1

	def print_graph(self):
		for i in range(self.numVertex):
			for j in range(self.numVertex):
				print(self.matrix[i][j], end = ' ')
			print("\n")
if __name__ == '__main__':
	G = Graph(5)

	G.set_edge(0,1,1)
	G.set_edge(0,4,1)

	G.set_edge(1,3,1)

	G.set_edge(2,4,1)

	G.set_edge(3,2,1)

	G.set_edge(4,1,1)
	G.print_graph()

