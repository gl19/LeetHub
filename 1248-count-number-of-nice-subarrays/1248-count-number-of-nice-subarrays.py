class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        num_odd = 0
        result = 0
        
        for num in nums:
            if num % 2 == 1:
                num_odd += 1
                
            result += count[num_odd - k]
            count[num_odd] += 1
        
        return result

                    
                


            

            



            


            