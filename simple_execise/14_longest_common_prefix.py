'''
#   breif   :    
#   history :   guo created 20210126
#   detail  :
                编写一个函数来查找字符串数组中的最长公共前缀。

                如果不存在公共前缀，返回空字符串 ""。
                 
                示例 1：

                输入：strs = ["flower","flow","flight"]
                输出："fl"
                示例 2：

                输入：strs = ["dog","racecar","car"]
                输出：""
                解释：输入不存在公共前缀。

                来源：力扣（LeetCode）
                链接：https://leetcode-cn.com/problems/longest-common-prefix
                著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
#   note    :  思路： 
                    step1: 异常剔除  是否有为空字符的情形。若有则返回""
                    step2: 所有str至少都有一个字符了,找出最短的那个str_short
                    step3: 遍历该str_short从i到len,然后去其它所有str进行比较即可


'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        # step1
        for  s in strs:
            if not s:
                return ""
        # step2:
        str_short = strs[0]
        for s in strs:
            if len(s) < len(str_short):
                str_short = s
        # step3
        for i in range(  len(str_short) ):  # 取strs[0]的index 
            for s in strs:
                if s[i] != str_short[i]:  # strs中每个str都取第i个元素，看与strs[0]的第i个元素是否相等 #TODO: 存在bug 可能 i 超过了某个s的下标
                    return str_short[0:i]
        return str_short

if __name__ == '__main__':
    import unittest
    class Test(unittest.TestCase):
        def test_all_case(self):
            S = Solution()
            # test 1:
            print(S.longestCommonPrefix(  ["flower","flow","flight"] ) )
            self.assertEqual(S.longestCommonPrefix(  ["flower","flow","flight"] ) , "fl")
            # test 2:
            print(S.longestCommonPrefix( ["dog","racecar","car"] ))
            self.assertEqual(S.longestCommonPrefix( ["dog","racecar","car"] ) , "")

            # rbg test 3:
            self.assertEqual(S.longestCommonPrefix(  ["flower","fl","flight"] ) , "fl")
    unittest.main()
