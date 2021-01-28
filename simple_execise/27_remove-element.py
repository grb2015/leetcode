'''
#   breif   :    
#   history :   guo created 20210128
#   detail  :
                给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

                不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

                元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

                示例 1:

                给定 nums = [3,2,2,3], val = 3,

                函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

                你不需要考虑数组中超出新长度后面的元素。
                示例 2:

                给定 nums = [0,1,2,2,3,0,4,2], val = 2,

                函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

                注意这五个元素可为任意顺序。

                你不需要考虑数组中超出新长度后面的元素。

                来源：力扣（LeetCode）
                链接：https://leetcode-cn.com/problems/remove-element
                著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

                #   note    :  思路： 
                                    不用管题目,直接开辟2个数组
                            


'''
class Solution(object):
    def removeElement(self, nums, val):
        nums2 = []
        for n in nums:
            if n != val:
                nums2.append( n )
        print(" nums2 = ")
        print(nums2)
        return len(nums2)


if __name__ == '__main__':
    import unittest
    class Test(unittest.TestCase):
        def test_all_case(self):
            S = Solution()
            # test 1:
            self.assertEqual(S.removeElement( [3,2,2,3] , 3 ) , 2)
            # test 2:
            self.assertEqual(S.removeElement( [0,1,2,2,3,0,4,2] , 2) , 5)
    unittest.main()
