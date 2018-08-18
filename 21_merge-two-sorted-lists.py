# -*- coding: utf-8 -*-
# @Author: Teiei
# @Date:   2018-08-18 20:57:30
# @Last Modified by:   Teiei
# @Last Modified time: 2018-08-18 22:49:21
# TODO: 算法效率比较低,leetcode排名很低，有待分析原因(自定义函数过多?)。
# 
# 
'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4


注意：再举个例子
   a = [1,2,3,6]
   b = [4,5]
   则输出[1,2,3,4,5,6]
   
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def get_link_len(head):
    p = head
    len = 0
    while(p != None):
        len += 1
        p = p.next
    return len


def get_link_val(head, index):
    p = head
    if(get_link_len(head) <= index):
        return None
    for i in range(index):
        p = p.next
    return p.val


def append_val(head, val):
    p = head
    while(p.next != None):
        p = p.next
    p.next = ListNode(val)


def insert_val(head, index, val):
    p = head
    print("-----------index = ", index)
    print("val =", val)
    len = get_link_len(head)
    if(len <= index):
        return None
    i = 0
    for i in range(index):
        print("p=pnext")
        p = p.next
    print("i = ", i, "len = ", len)
    print("p.val =", p.val)
    if i == len - 1:  # insert to tail
        p.next = ListNode(val)
    else:
        tmp = p.next.next
        p.next = ListNode(val)
        p.next.next = tmp
    return head


def print_link(head):
	p = head
	while(p != None):
		print(p.val, end=" ")
		p = p.next


class Solution:

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        p1 = l1
        i = 0
        len1 = get_link_len(l1)
        len2 = get_link_len(l2)
        #print("len1 = ", len1)
        #print("len2 = ", len2)
        l3 = ListNode(-1)

        pos1 = 0
        pos2 = 0
        for i in range(len1 + len2):
            if pos1 <= len1-1 and pos2 <= len2-1:
                val1 = get_link_val(l1, pos1)
                val2 = get_link_val(l2, pos2)
                if(val1 < val2):
                	append_val(l3, val1)
                	#print("pos1 = ",pos1,"val1=",val1)
                	pos1 += 1 
                else:
                	append_val(l3, val2)
                	#print("pos2 = ",pos2,"val2=",val2)
                	pos2 += 1
                    
            else:
            	#print("pos1 = ", pos1)
            	#print("pos2 = ", pos2)
            	print_link(l3.next)
            	break
        if(pos1 <= len1-1):
            for i in range(pos1, len1):
                val1 = get_link_val(l1, i)
                append_val(l3, val1)
        if(pos2 <= len2-1):
            for i in range(pos2, len2):
                val2 = get_link_val(l2, i)
                append_val(l3, val2)
        #print("pos1 = ",pos1)
        #print("pos2 = ",pos2)
        print_link(l3.next)
        return l3.next
