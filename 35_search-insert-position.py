# -*- coding: utf-8 -*-
# @Author: Teiei
# @Date:   2018-08-21 20:57:04
# @Last Modified by:   Teiei
# @Last Modified time: 2018-08-21 21:25:10
# https://leetcode-cn.com/problems/search-insert-position/description/
'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0
'''
# 算法思路：遍历nums,寻找nums中连续2个数，左边那个数小于target
#           右边那个数>=target ,然后判断,如果是等于，这返回右边的数的Index
#           如果是大于,其实也是返回右边的数的Index
#


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[0] >= target:
            return 0
        if nums[-1] == target:
            return len(nums)-1
        if nums[-1] < target:
            return len(nums)
        for i in range(len(nums)-1):
            #print("i = ",i)
            #print(nums[i])
            #print(nums[i+1])
            if nums[i] < target and nums[i+1] >= target:
                return i+1
        #print("in -1")
        print(" returned None !")
        return None  # 没找到,应该是永远到不了这里


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 5))
    print(s.searchInsert([1, 3, 5, 6], 2))
    print(s.searchInsert([1, 3, 5, 6], 7))
    print(s.searchInsert([1, 3, 5, 6], 0))
    #print("----------------")
    print(s.searchInsert([1, 3], 2))
