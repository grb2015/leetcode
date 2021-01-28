'''
#   breif   :    
#   history :   guo created 20210128
#   detail  :
                给定一个正整数 n ，输出外观数列的第 n 项。

                「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。

                1.     1
                2.     11
                3.     21
                4.     1211
                5.     111221
                第一项是数字 1 
                描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
                描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
                描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
                描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"

                输入：n = 1
                输出："1"
                解释：这是一个基本样例。
                示例 2：

                输入：n = 4
                输出："1211"

                来源：力扣（LeetCode）
                链接：https://leetcode-cn.com/problems/count-and-say
                著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

                #   note    :  思路： 
                #               解释一下题目：
                #                   n = 1 是固定的为  1
                #                   n = 2 是对前一项的描述,因为前1项为1个1 , 所以输出为11
                                    n = 3 是对11进行描述，为2个1 所以输出为21
                                    n = 4 是对21进行描述  ，为1个2，1个1 ，所以输出为1211
                                    n = 5 是对1211进行描述 ， 为3个1,1个2,你可能觉得为3112。这里有个规则就是3个1必须是连续的才算，中断了要重新计算。
                                            所以为1个1,1个2,2个1分三段 ，输出为111221
                                step1:  n = 0  不考虑这种情况
                                        n = 1  返回 "1"
                                step2：
                                    如果n = 10 , 我们计算的时候，其实需要把前10项计算出来。
                                    开辟一个数组来存储每一项。
                                    一个for 循环10 次，每次计算第i项.
                                    计算某一项的时候,比如第10项，那就看第九项即可
                            


'''
###################################################################
#   breif   :   根据前一项计算当前项的值
#   inputs  :   pre_str   [str]   前一项的值
#   returns ：  cur_str   [str]   当前项的值
#   detail  :   思路：比如pre_str = "111221"
#                   给i,j两个指针,进行遍历 pre_str。 [i,j]之间都是连续一样的值。比如三个2 ，那么i,j这一段就是 32
#                   所以第一次[i,j] = [0,2] = "111" => "31" 就给"31" append到cur_str里面。然后i后移到index = 3的位置，j从i的位置遍历到"22"这段。
#                   什么时候终止，就是i不超过最后一个元素。
#               
# 
# 
# 
####################################################################
def get_value_from_pre(pre_str):
    print(" ### [get_value_from_pre] pre_str = ",pre_str)
    i = 0
    cur_str = ""
    while( i < len( pre_str ) ):
        j = i 
        while( j < len( pre_str ) and  pre_str[j] == pre_str[i] ):
            j += 1
        cur_str += str(len( pre_str[i:j] ) ) + pre_str[i]  ##  pre_str[i:j] = "111" ==> "31"
        i = j
    return cur_str

class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"
        else:
            result_list = []
            for i in range( n ):
                if not result_list: # 等价于 i = 0
                    result_list.append("1")
                else:
                    pre_str = result_list[i-1]
                    cur_str = get_value_from_pre(pre_str)
                    print("cur_str = ",cur_str)
                    result_list.append(cur_str)
        print("result_list = ")
        print(result_list)
        return result_list[n-1]


if __name__ == '__main__':
    import unittest
    class Test(unittest.TestCase):
        def test_all_case(self):
            S = Solution()
            # test 1:
            self.assertEqual(S.countAndSay(1) , "1")
            # test 2:
            self.assertEqual(S.countAndSay(4) , "1211")
    unittest.main()
