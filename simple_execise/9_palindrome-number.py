'''
#   breif   :    
#   history :   guo created 20210126
#   detail  :
                判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

                示例 1:

                输入: 121
                输出: true
                示例 2:

                输入: -121
                输出: false
                解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
                示例 3:

                输入: 10
                输出: false
                解释: 从右向左读, 为 01 。因此它不是一个回文数。

                来源：力扣（LeetCode）
                链接：https://leetcode-cn.com/problems/palindrome-number
                著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
#   note    :  

'''
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            str_x = str(x)
            for i in range(len(str_x)):
                if str_x[i] != str_x[len(str_x)-1-i]:
                    return False
            return True
if __name__ == '__main__':
    import unittest
    class Test(unittest.TestCase):
        def test_all_case(self):
            S = Solution()
            # test 1:
            print( S.isPalindrome(121) )
            self.assertEqual(S.isPalindrome(121) , True)
            # test 2:
            print( S.isPalindrome(-121) )
            self.assertEqual(S.isPalindrome(-121) , False)
            # test 3:
            print( S.isPalindrome(10) )
            self.assertEqual(S.isPalindrome(10) , False)
    unittest.main()
