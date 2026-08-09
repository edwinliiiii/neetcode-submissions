class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        
        keep a map of { anagram -> [strings]}

        time O(n*m)
        space O(n*m)

        n = len of strs
        m = length of any arbitrary s in strs

        '''

        groupedAnagrams = {}

        for s in strs: # O(n)
            frequency_map = dict(Counter(s)) # freq map O(m)
            sortedFreqMap = dict(sorted(frequency_map.items())) #sorted freq map O(26) then O(26)
            identifier = self.stringifySortedFreqMap(sortedFreqMap)

            groupedAnagrams.setdefault(identifier, []).append(s)

        return list(groupedAnagrams.values());


    # return a string identifier for how we group anagrams together
    def stringifySortedFreqMap(self, d):
        ans = ""
        for letter, freq in d.items():
            ans += (letter + str(freq))
        return ans;
