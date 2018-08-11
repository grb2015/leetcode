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

version2: 20180811 改进，精简代码

'''
class Solution:
    def isValid(self, s):
        stack = []
        dict_prths = {'(':')','[':']','{':'}'} 
        for char in s:
            if char in dict_prths.keys(): # 左括号入栈
                stack.append(char)
            else: # 非左括号(右括号或者其他非法字符），与pop比较
                if len(stack) == 0 or dict_prths[stack.pop()] != char:
                    return False
        return len(stack)==0 ## for "{{"
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

