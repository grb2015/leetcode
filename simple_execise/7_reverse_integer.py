'''
#   breif   :    
#   history :   guo created 20210125
#   detail  :
                给你一个 32 位的有符号整数 x ，返回 x 中每位上的数字反转后的结果。

                如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。

                假设环境不允许存储 64 位整数（有符号或无符号）。
                 

                示例 1：
                输入：x = 123
                输出：321

                示例 2：
                输入：x = -123
                输出：-321

                示例 3：
                输入：x = 120
                输出：21

                示例 4：
                输入：x = 0
                输出：0

                来源：力扣（LeetCode）
                链接：https://leetcode-cn.com/problems/reverse-integer
                著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
#   note    :  
                思路：
                    先考虑符号 x =  -123   str(x) =  '-123'   如果是负号，就不要反转负号了
                    其次考虑120这种情况, str(120)= '012', int('012') = 12  正常处理即可
'''

##########################################
#   breif   :   判断某个正数是否超出32位整数的范围
#   input   :   [int] x   
#   output  :   [bool] 超出返回true , 没有超出返回false
##########################################
def is_over_32int(x):
    if x > 2**31 -1 or x < -1*(2**31):
        return True
    else:
        return False

##########################################
#   breif   :   反转一个正数
#   input   :   [int] x   
#   output  :   [int] 反转后的
##########################################
def reverse_positive(x):
    str_x = str(x)
    str_x_reverse = str_x[::-1]
    int_x_reverse = int(str_x_reverse)
    if is_over_32int(int_x_reverse):
        return 0
    return int_x_reverse

class Solution(object):
    def reverse(self, x):
        if x >= 0:
            return reverse_positive(x)
        else:   # 是负数
            abs_x = abs(x)
            return -1*reverse_positive( abs_x )

if __name__ == '__main__':

    # test1 
    x = 123
    S = Solution()
    print("输入为%d：期望输出：321"%(x))
    print(S.reverse(x))


    # test2
    x = -123
    print("输入为%d：期望输出：-321"%(x))
    print(S.reverse(x))


    # test3
    x = 120
    print("输入为%d：期望输出：21"%(x))
    print(S.reverse(x))

    # test4
    x = 0
    print("输入为%d：期望输出：0"%(x))
    print(S.reverse(x))


    #  test is_over_32int
    print( is_over_32int(2147483651) )