import itertools

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        naive: n log n

        make a freq map,
        sort by value,
        then take first k as the answer

        '''
        freq_map = Counter(nums)
        sorted_by_value = dict(sorted(freq_map.items(), key=lambda item: item[1], reverse=True))

        keys_sorted = list(sorted_by_value.keys())

        return keys_sorted[0:k]
