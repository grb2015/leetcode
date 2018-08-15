class Node(object):
	"""docstring for Node"""
	def __init__(self, val,next = None):
		self.val = val
		self.next= next
class Link(object):
	"""docstring for Link"""
	def __init__(self, head,length):
		self.head = head
		self.length = length
	def add_node(self,val):
		if self.head == None:
			self.head = Node(val)
		else:
			p = self.head
			while(p.next != None):
				p = p.next
			p.next = Node(val)
		self.length += 1
	
	'''
	brief  :     get the indexth Node value of Link 
	returns:
		None : if index > length
		val  : the indexth Node value of Link 
	'''
	def get_node(self,index):
		if self.length < index:
			print("index is beyond link length:{}".format(self.length))
			return None
		else:
			p = self.head
			for i in range(index):
				p = p.next
			return p.val

	def print_link(self):
		p = self.head
		while(p != None):
			print(p.val)
			p = p.next


if __name__ == '__main__':
	head = None
	length = 0
	L = Link(head,length)
	L.add_node(3)
	L.add_node(4)
	L.add_node(5)
	L.print_link()
	print(L.get_node(1))


		
		