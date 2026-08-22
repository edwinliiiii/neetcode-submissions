import itertools

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        naive: n log n

        make a freq map,
        sort by value,
        then take first k as the answer

        --------------

        freq_map = Counter(nums)
        sorted_by_value = dict(sorted(freq_map.items(), key=lambda item: item[1], reverse=True))

        keys_sorted = list(sorted_by_value.keys())

        return keys_sorted[0:k]

        '''

        '''

        non naive solution: bucket sort
        allocate a size-n+1 list where the index represents # of occurrences.

        count freq map O(n), then add each element to appropriate bucket O(n),

        [1, 2, 2, 3, 3, 3]
        size-n+1 list (for ease of index purposes)
        0.   1    2    3    4    5    6.  
             [1]. [2]. [3]. X.   X    X
        SPACE O(n). with n worst case values to fill in the n buckets.
        worst case would look like 1 value in each of the n buckets, so n values.

        then iterate over the n buckets backwards and take all values until k is reached O(n)

        total time: O(n) + O(n) + O(n) = 3 O(n) = O(n)
        tote space: O(n) + O(n) + O(n) = 3 O(n) = O(n)
        '''

        freq_map = Counter(nums)
        buckets = [[] for i in range(len(nums)+1)]

        for key, value in freq_map.items():
            buckets[value].append(key)
        
        ans = []
        
        for values in buckets[::-1]:
            for value in values:
                ans.append(value)
                if len(ans) >= k:
                    return ans
        
        return ans



        
