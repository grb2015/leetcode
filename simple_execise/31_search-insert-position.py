'''
#   breif   :    
#   history :   guo created 20210128
#   detail  :
                给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

                你可以假设数组中无重复元素。

                示例 1:

                输入: [1,3,5,6], 5
                输出: 2
                示例 2:

                输入: [1,3,5,6], 2
                输出: 1
                示例 3:

                输入: [1,3,5,6], 7
                输出: 4
                示例 4:

                输入: [1,3,5,6], 0
                输出: 0

                来源：力扣（LeetCode）
                链接：https://leetcode-cn.com/problems/search-insert-position
                著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

                #   note    :  思路： 
                                step1:异常处理
                                        如果nums为[] 返回0
                                step2：
                                    只需要遍历一遍即可啊，很简单.
                                    如果遍历到尾部，还没有的话，就返回len(nums)
                            


'''
class Solution(object):
    def searchInsert(self, nums, target):
        if not nums:
            return 0
        for i in range( len(nums) ):
            if nums[i] >= target:
                return i
        return len(nums)


if __name__ == '__main__':
    import unittest
    class Test(unittest.TestCase):
        def test_all_case(self):
            S = Solution()
            # test 1:
            self.assertEqual(S.searchInsert( [1,3,5,6] ,5 ) , 2)
            # test 2:
            self.assertEqual(S.searchInsert( [1,3,5,6] , 2) , 1)
            # test 3:
            self.assertEqual(S.searchInsert( [1,3,5,6] , 7) , 4)
            # test 4:
            self.assertEqual(S.searchInsert( [1,3,5,6] , 0) , 0)
    unittest.main()
