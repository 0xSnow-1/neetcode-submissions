class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Mappy = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in Mappy:
                return [Mappy[diff], i]
            Mappy[n] = i
            




        
        
            
             

            
             
        
        