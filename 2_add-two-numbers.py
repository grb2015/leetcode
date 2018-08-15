#https://leetcode-cn.com/problems/add-two-numbers/description/
'''
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807


'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
    思路： 先从l1中将所有的value取出来，组成一个字符串str1
	   同样l2 组成str2
	   再将str1 和 str2相加(要转为int才能加, 有可能链表有几百个节点，这时候有可能超过python表示的数据范围,可能有Bug)
	   然后在将相加的结果组建为一个新的链表。
    TODO: 转为Int求和可能有Bug
'''
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        str1  = ""
        str2  = ""
	# 提取l1中的val组成字符串str1
        while(p1 != None):
        	str1 = str1+str(p1.val)
        	#print(p1.val)
        	p1 = p1.next
        	
        print('----------------')
        p2 = l2
	# 提取l2中的val组成字符串str2
        while(p2 != None):
        	str2 = str2+str(p2.val)
        	#print(p2.val)
        	p2 = p2.next
        #print(str1)
        #print(str2)
	#相加 str1+str2
        sum_str = str( int(str1[::-1]) + int(str2[::-1]) )
        #print(sum_str)

	# 用所得的和组建新链表
        head = ListNode(-1) 
        p = head
        for c in sum_str[::-1]:
        	p.next = ListNode(c)
        	p = p.next
        return head.next

