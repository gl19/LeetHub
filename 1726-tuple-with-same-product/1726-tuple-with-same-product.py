class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        products = defaultdict(list)
        for num1 in nums:
            for num2 in nums:
                if num1 != num2:
                    products[num1 * num2].append((num1, num2))
        
        pairs = 0
        for product in products.keys():
            for pair1 in products[product]:
                for pair2 in products[product]:
                    if (pair1[0] not in pair2) and (pair1[1] not in pair2):
                        pairs += 1

        return pairs

