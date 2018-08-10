'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
'''
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict_prths = {'(':')','[':']','{':'}'}  # dict parentheses
        s_left  = []  # stored all the left parenthes in s 
        s_right = []  # right 
        for c in s:
        	if c in dict_prths.keys():
        		s_left.append(c)
        	elif c in dict_prths.values():
        		s_right.append(c)
        	else:
        		print("invaid input ")
        		return False
        if len(s_left) != len(s_right):
        	return False
        for i in range(len(s_left)):
        	if dict_prths[s_left[i]] != s_right[i]:
        		return False
        return True 
if __name__ == '__main__':
	s = Solution()
	print(s.isValid("()") )  # True
	print(s.isValid("()[]{}")) # True
	print(s.isValid("(]"))    #False
	#这种算法是有问题，处理这两个用例会出错
	print(s.isValid("([)]")) # False   
	print(s.isValid("{[]}")) # True   

