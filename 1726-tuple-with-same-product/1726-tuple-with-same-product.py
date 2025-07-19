class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        products = defaultdict(list)
        dedup = list(dict.fromkeys(nums))
        dedup.sort()
        for i, num1 in enumerate(dedup):
            for num2 in dedup[i + 1:]:
                products[num1 * num2].append((num1, num2))
        
        pairs = 0
        for product in products.keys():
            if len(products[product]) > 1:
                pairs += 2 ** (len(products[product]) + 1)

        return pairs

