class Solution:
    def num_pairs(self, n):
        return sum([i for i in range(1, n)])

    def tupleSameProduct(self, nums: List[int]) -> int:
        products = defaultdict(list)
        dedup = list(dict.fromkeys(nums))
        for i, num1 in enumerate(dedup):
            for num2 in dedup[i + 1:]:
                products[num1 * num2].append((num1, num2))
        
        pairs = 0
        for product in products.keys():
            n = len(products[product])
            if n > 1:
                pairs += 8 * self.num_pairs(n)

        return pairs