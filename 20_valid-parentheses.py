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

'''
每当遇到一个右侧符号时，检查栈是否为空(右括号不入栈)，若此时栈不为空.
则对栈进行pop操作表明顶部元素已被匹配，否则为不匹配情况.
直接返回false .当整个字符串遍历结束，我们就可以通过判断该栈是否为空来判断整个字符串中的符号是否匹配
'''
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if(len(s) == 0):  ## for ""
        	return True
        dict_prths = {'(':')','[':']','{':'}'}  # dict parentheses
        s_left  = []  # stored all the left parenthes in s 
        s_right = []  # right 

        for c in s:
        	if c not in dict_prths.keys() and c not in dict_prths.values():
        		return False
       	stack = []   # python中栈可以就是list 
        for i in range(len(s)):
        	if s[i] in dict_prths.keys():
        		stack.append(s[i])
        	elif  s[i] in dict_prths.values():
        		if len(stack) > 0:
        			if dict_prths[stack.pop()] != s[i]:
        				return False
        		else: ## for "))"
        			return False
        	else:
        		return False
        return False if  len(stack) > 0  else  True  ## for "((" 
s = Solution()
print(s.isValid("()") )  # True
print(s.isValid("()[]{}")) # True
print(s.isValid("(]"))    #False
print(s.isValid("([)]")) # False   
print(s.isValid("{[]}")) # True   
print(s.isValid("[")) # False   
print(s.isValid("")) # True  
print(s.isValid("((")) # False  
print(s.isValid("}}")) # False  
print(s.isValid("}}ddd")) # Flase  

