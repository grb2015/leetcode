# https://leetcode-cn.com/problems/find-the-duplicate-number/description/
'''
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。
'''


'''
以下是时间复杂度为O(n)的解法: 这是一次真实的C面试题，python简单多了
'''
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_count = {}
        for num in nums:
        	if num in dict_count:  ## or dict_count[num] = dic.get(num, 0) + 1
        		return num
        	else:
        		dict_count[num] = 1	## or if dic[num] >= 2
        print("no dup num in nums")
        return -1  
if __name__ == '__main__':
	s = Solution()
	nums = [1,3,4,2,2]
	print(s.findDuplicate(nums))
	nums = [3,1,3,4,2]
	print(s.findDuplicate(nums))

