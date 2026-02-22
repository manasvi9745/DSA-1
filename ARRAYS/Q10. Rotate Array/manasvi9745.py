from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n   # Handle cases where k > n
        
        # Step 1: Reverse entire array
        self.reverse(nums, 0, n - 1)
        
        # Step 2: Reverse first k elements
        self.reverse(nums, 0, k - 1)
        
        # Step 3: Reverse remaining elements
        self.reverse(nums, k, n - 1)
    
    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
