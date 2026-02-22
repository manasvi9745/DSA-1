from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        
        for i in range(len(nums)):
            # If we can't reach this index
            if i > farthest:
                return False
            
            # Update farthest reachable index
            farthest = max(farthest, i + nums[i])
            
            # Early exit if we can reach last index
            if farthest >= len(nums) - 1:
                return True
        
        return True
