'''
#   breif   :    
#   history :   guo created 20210128
#   detail  :
                给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

                不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

                 

                示例 1:

                给定数组 nums = [1,1,2], 

                函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 

                你不需要考虑数组中超出新长度后面的元素。
                示例 2:

                给定 nums = [0,0,1,1,1,2,2,3,3,4],

                函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

                你不需要考虑数组中超出新长度后面的元素。

                来源：力扣（LeetCode）
                链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
                著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

                #   note    :  思路： 
                                    不用管题目,直接开辟2个数组
                            


'''
class Solution(object):
    def removeDuplicates(self, nums):   
        nums2 =  []
        for  n in nums:
            if n not in nums2:
                nums2.append(n)
        print("nums2 = ")
        print(nums2)
        return len(nums2)

if __name__ == '__main__':
    import unittest
    class Test(unittest.TestCase):
        def test_all_case(self):
            S = Solution()
            # test 1:
            self.assertEqual(S.removeDuplicates( [1,1,2] ) , 2)
            # test 2:
            self.assertEqual(S.removeDuplicates( [0,0,1,1,1,2,2,3,3,4] ) , 5)
    unittest.main()
