class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_occurances = Counter(arr)
        return len(num_occurances) == len(set(num_occurances.values()))
