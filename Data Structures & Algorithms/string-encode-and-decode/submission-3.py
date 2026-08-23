class Solution:

    '''

    join list of strings w/ delimit probably. white space should be preserved

    main problem: how to guarantee a unique delimit?
    - something outside of 256 ASCII chars?
    - delimit is length of the next string?
        - ["apple", "orange", "pieeeeeeee"] -> 15apple16orange210pie
        - but when len of str is more than 1 digit, gets hairy.
        - have first int indicate how many digits the length is (always 1, 2, or 3) 
            as 0 <= strs[i].length < 200
    '''

    # ["apple", "orange", "pieeeeeeee"] -> 15apple16orange210pie
    def encode(self, strs: List[str]) -> str:
        ans = ''    
        for s in strs:
            length = len(s)
            numLengthDigits = str(self.numLengthDigits(length))
            ans+=numLengthDigits+str(length)
            ans+=s

        return ans

    def numLengthDigits(self, i: int) -> int:
        return len(str(i))

    # 15apple16orange210pie -> ["apple", "orange", "pieeeeeeee"]
    def decode(self, s: str) -> List[str]:
        ans = []
        startIndex=0
        while startIndex < len(s): 
            lengthOfLength = int(s[startIndex])
            lengthOfString = int(s[startIndex+1:startIndex+1+lengthOfLength])

            startIndexOfString = startIndex+self.numLengthDigits(lengthOfLength)+self.numLengthDigits(lengthOfString)
            ans.append(s[startIndexOfString:startIndexOfString+lengthOfString])
            startIndex = startIndexOfString+lengthOfString

        return ans
