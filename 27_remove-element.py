# -*- coding: utf-8 -*-
# @Author: Teiei
# @Date:   2018-08-19 21:55:58
# @Last Modified by:   Teiei
# @Last Modified time: 2018-08-19 22:39:12

# https://leetcode-cn.com/problems/remove-element/description/
'''
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
实例：
给定 nums = [0,1,2,2,3,0,4,2], val = 2,

函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

注意这五个元素可为任意顺序。

你不需要考虑数组中超出新长度后面的元素。
'''

'''修改题目：可以开辟新空间 '''

#note :一种错误的解法(该解法没有考虑到nums的值改变后，原来Nums的长度会变，会影响迭代)：
'''
class Solution:
    def removeElement(self, nums, val):
        for n in nums:
        	if n == val:
        		nums.remove(val)  
'''

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        val_index = [] ## 记录要所有值为val的元素的下标
        for i, n in enumerate(nums):
        	if n == val:
        		val_index.append(i)
        for i in val_index[::-1]: ## 必须从后向前删除，不然nums长度变了,pop(i)可能就会超出下标
        	nums.pop(i)


if __name__ == '__main__':
    s = Solution()
    num = [0, 1, 2, 2, 3, 0, 4, 2,2]
    val = 2
    print(num)
    s.removeElement(num, val) ## 这里会改变num的值，list可变，故是传址
    print(num)  ## 这里

