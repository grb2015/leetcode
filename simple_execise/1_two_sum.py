'''
#   breif   :   https://leetcode-cn.com/problems/two-sum/
#   history :   guo created 20210125
#   detail  :
            给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
            你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
            你可以按任意顺序返回答案。


            示例 1：

            输入：nums = [2,7,11,15], target = 9
            输出：[0,1]
            解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
            示例 2：

            输入：nums = [3,2,4], target = 6
            输出：[1,2]
            示例 3：

            输入：nums = [3,3], target = 6
            输出：[0,1]

            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/two-sum
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
#   note    : 
'''

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j
if __name__ == '__main__':
    # test 1
    nums1 = [2,7,11,15]
    target1 = 9
    s1 = Solution()
    print(s1.twoSum(nums1,target1))

    # test2
    nums1 = [3,2,4]
    target1 = 6
    s1 = Solution()
    print(s1.twoSum(nums1,target1))

    # test3
    nums1 = [3,3]
    target1 = 6
    s1 = Solution()
    print(s1.twoSum(nums1,target1))
        