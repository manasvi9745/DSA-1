class Solution:
    def maxSumMinProduct(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        
        # Step 1: Prefix Sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        # Step 2: Find boundaries using Monotonic Stack
        stack = []
        max_product = 0
        
        for i in range(n + 1):
            while stack and (i == n or nums[stack[-1]] > nums[i]):
                mid = stack.pop()
                left = stack[-1] if stack else -1
                right = i
                
                subarray_sum = prefix[right] - prefix[left + 1]
                max_product = max(max_product, nums[mid] * subarray_sum)
            
            stack.append(i)
        
        return max_product % MOD
