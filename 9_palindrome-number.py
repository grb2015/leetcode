class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x< 0:
        	return False
        str_x = str(x)
        str_x_len = len(str_x)
        for i in range(str_x_len//2+1):
        	if str_x[i] != str_x[str_x_len-1-i]:
        		return False
        return True
if __name__ == '__main__':
	s = Solution()
	xs = [-123,0,12321]
	for x in xs:
		print(s.isPalindrome(x))
