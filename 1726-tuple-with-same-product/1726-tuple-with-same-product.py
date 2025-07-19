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
            for pair1 in products[product]:
                for pair2 in products[product]:
                    if (pair1[0] not in pair2) and (pair1[1] not in pair2):
                        pairs += 4

        return pairs

