class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # First, gather the frequencies of letter occurrences in s
        freq = {}
        for letter in s:
            if letter in freq:
                freq[letter] = freq[letter] + 1
            else:
                freq[letter] = 1
        
        for letter in t:
            if letter not in freq or freq[letter] <= 0:
                return False
            else:
                freq[letter]-=1

        for value in freq.values():
            if value >= 1:
                return False
                
        return True
