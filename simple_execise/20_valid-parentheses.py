'''
#   breif   :    
#   history :   guo created 20210127
#   detail  :
                给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

                有效字符串需满足：

                左括号必须用相同类型的右括号闭合。
                左括号必须以正确的顺序闭合。
                 

                示例 1：

                输入：s = "()"
                输出：true
                示例 2：

                输入：s = "()[]{}"
                输出：true
                示例 3：

                输入：s = "(]"
                输出：false
                示例 4：

                输入：s = "([)]"
                输出：false
                示例 5：

                输入：s = "{[]}"
                输出：true

                注意：1 <= s.length <= 104 

                来源：力扣（LeetCode）
                链接：https://leetcode-cn.com/problems/valid-parentheses
                著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#   note    :  思路： 
                   

                    step1:  异常情况
                            1.判断s是否为空字符串。若是，返回True.
                            2.判断s是否长度为1。若是,则返回False
                    step2:  现在长度至少为2了。
                                使用栈的数据结构。每次遇到右括号,就与栈顶元素比较。
                                1.可能遇到右括号时，栈为空。此时返回False
                                2.可能遍历完了后，栈还不为空，此时返回False
                                综合1,2 ： 当且仅当遍历完字符串后，栈为空。返回True
                            


'''
class Solution(object):
    def isValid(self, s):
        # step1
        if not s:  # s为空字符串
            return True
        if len(s) == 1:
            return False
        for item in s:
            if item not in ['(',')','[',']','{','}']:
                return False
        # step2:
        stack = []
        for item in s:
            if item in ['(','[','{']:
                stack.append(item)
            else:
                if not stack:
                    return False
                if item == ')' and stack[-1] == '(':
                    stack.pop(-1)
                elif item == ']' and stack[-1] == '[':
                    stack.pop(-1)
                elif item == '}' and stack[-1] == '{':
                    stack.pop(-1)
                else:
                    return False
        if stack:
            return False
        else:
            return True


if __name__ == '__main__':
    import unittest
    class Test(unittest.TestCase):
        def test_all_case(self):
            S = Solution()
            # test 1:
            self.assertEqual(S.isValid( "()") , True)
            # test 2:
            self.assertEqual(S.isValid(  "()[]{}" ) , True)
            # test 3:
            self.assertEqual(S.isValid(  "(]" ) , False)
            # test 4:
            self.assertEqual(S.isValid(  "([)]" ) , False)
            # test 5:
            self.assertEqual(S.isValid(  "{[]}" ) , True)
    unittest.main()
