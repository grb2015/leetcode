class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]
if __name__ == '__main__':
	s = Solution()
	xs = [-123,0,12321]
	for x in xs:
		print(s.isPalindrome(x))
