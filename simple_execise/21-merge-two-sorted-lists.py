'''
#   breif   :    
#   history :   guo created 20210127
                将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
                输入：l1 = [1,2,4], l2 = [1,3,4]
                输出：[1,1,2,3,4,4]
                示例 2：

                输入：l1 = [], l2 = []
                输出：[]
                示例 3：

                输入：l1 = [], l2 = [0]
                输出：[0]

                来源：力扣（LeetCode）
                链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
                著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#   note    :  思路： 
                   

                    step1:  异常情况
                            1.若L1为空,则返回L2
                            2.如L2为空,则返回L1
                    step2:  现在L1,L2都不为空了。
                                新开辟一个list存放结果
                                i,j两个指针取遍历L1,L2即可
                                1.当i遍历完后，j没有遍历完。则将 [j,len(l2)]的所有值插入
                                2.同理对j
                            


'''
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        # step1: 
        if not l1:
            return l2
        if not l2:
            return l1
        # step2:
        rt_list = []
        i = 0
        j = 0
        while i<len(l1) and j<len(l2):
            if l1[i] < l2[j]:
                rt_list.append( l1[i] )
                i += 1
            else:
                rt_list.append( l2[j] )
                j += 1 
        if i == len(l1):
            while j < len(l2):
                rt_list.append( l2[j])
                j += 1
        if j == len(l2):
            while i < len(l1):
                rt_list.append( l1[i] )
                i += 1
        return rt_list



if __name__ == '__main__':
    import unittest
    class Test(unittest.TestCase):
        def test_all_case(self):
            S = Solution()
            # test 1:
            self.assertEqual(S.mergeTwoLists( [1,2,4],[1,3,4] ), [1,1,2,3,4,4])
            # test 2:
            self.assertEqual(S.mergeTwoLists(  [],[] ) , [])
            # test 3:
            self.assertEqual(S.mergeTwoLists(  [],[0] ) , [0])
    unittest.main()
