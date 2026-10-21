class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''

        2 pointer. denote p1 to first index, and p2 to last index. continuously move them toward each other, checking if chars are equal, until 

        '''


        cleaned_s = ''.join(char for char in s if char.isalnum())


        p1 = 0
        p2 = len(cleaned_s)-1

        while p2 > p1:
            if cleaned_s[p1].lower() != cleaned_s[p2].lower():
                return False
            p1+=1
            p2-=1
        
        return True