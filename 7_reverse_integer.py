def is_value_in_int32(x):
	return -(2**31) <= x <2**31-1
class Solution:
	def reverse(self, x):
		"""
        :type x: int
        :rtype: int
        """
		if  not is_value_in_int32(x):
			print("intput number  x not in int32 : x = ",x)
			return 0
		sign = [-1,1][x>0] #判断x的正负
		rx = sign*int(str(abs(x))[::-1]) # int->str->反转-->int
		
		if not is_value_in_int32(rx):
			print("result number  rx not in int32 : rx = ",rx)
			return 0
		return rx
if __name__ == '__main__':
    s = Solution()
    print(s.reverse(9876543210))
    print(s.reverse(-123))
    print(s.reverse(1234567899))
