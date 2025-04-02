'''
Runtime 3 ms | Beats 88.45% :feels-good:
Memory 17.73 MB | Beats 63.79% :mmm:
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return True if str(x) == str(x)[::-1] else False
