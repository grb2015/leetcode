'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀
'''

'''
算法思路：
	拿strs = ["flower","flow","flight"] 来说,
	先取flower的flower[0:1] 然后遍历strs,看其它str的[0:1]字符串是否都为[l]
	然后取flower的flower[0:2]... 
	
'''
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ## 先计算出最短的字符串的长度min_len
        if strs == []:
            print("input is []")
            return ""
        lens = []
        for str in strs:
            lens.append(len(str))
        lens.sort()
        min_len = lens[0]

        ## 从0-min_len 对strs[0]遍历
        for pos in range(0,min_len):
            for str in strs:
                if strs[0][:pos+1] != str[:pos+1]:
                    return "" if pos == 0 else str[:pos]
        return strs[0][:min_len]  ## 如果比较完了min_len都还没找到差异，那么return strs[0][:min_len] 
if __name__ == '__main__':
	s = Solution()
	print(s.longestCommonPrefix(["flower","flow","flight"]) )
	print(s.longestCommonPrefix(["dog","racecar","car"]) )
	print(s.longestCommonPrefix(['a','b']))