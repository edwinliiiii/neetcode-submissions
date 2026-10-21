class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        2 pointer. denote p1 to first index, and p2 to last index. continuously move them toward each other, checking if chars are equal. skip index if it's not alphanumeric
        '''
        

        p1 = 0
        p2 = len(s)-1

        while p2 > p1:
            while p1 < p2 and not s[p1].isalnum():
                p1+=1
            while p2 > p1 and not s[p2].isalnum():
                p2-=1
            if s[p1].lower() != s[p2].lower():
                return False
            p1+=1
            p2-=1
            
        return True
        
        
        
        
        
        
        '''
        2 pointer. denote p1 to first index, and p2 to last index. continuously move them toward each other, checking if chars are equal 

        O(n) time and space. make it O(1) space.


        cleaned_s = ''.join(char for char in s if char.isalnum()) # O(n)

        p1 = 0
        p2 = len(cleaned_s)-1

        while p2 > p1: # O(n)
            if cleaned_s[p1].lower() != cleaned_s[p2].lower():
                return False
            p1+=1
            p2-=1
        
        return True
        '''