class Solution:
    def num_pairs(self, n):
        return sum([i for i in range(1, n)])

    def tupleSameProduct(self, nums: List[int]) -> int:
        products = defaultdict(int)
        dedup = list(dict.fromkeys(nums))
        for i, num1 in enumerate(dedup):
            for num2 in dedup[i + 1:]:
                products[num1 * num2] += 1
        
        total_pairs = 0
        for n in products.values():
            if n > 1:
                total_pairs += 8 * self.num_pairs(n)

        return total_pairs