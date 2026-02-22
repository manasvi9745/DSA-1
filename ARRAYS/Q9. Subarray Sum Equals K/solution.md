# Q9. Subarray Sum Equals K

**LeetCode Problem:** Subarray Sum Equals K  

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the total number of **continuous subarrays** whose sum equals `k`.

---

## Sample Test Cases

**Input:**  
`nums = [1,1,1], k = 2`  
**Output:**  
`2`

**Input:**  
`nums = [1,2,3], k = 3`  
**Output:**  
`2`

---

## Approach

This problem is solved using the **Prefix Sum** technique along with an `unordered_multiset`.

### Key Idea
- Let `sum` be the prefix sum up to the current index.
- If there exists a previous prefix sum equal to `sum - k`, then the subarray between those indices sums to `k`.
- Since the same prefix sum can occur multiple times, an `unordered_multiset` is used to store all prefix sums and count their occurrences.

### Steps
1. Initialize a multiset and insert `0` to handle subarrays starting from index `0`.
2. Traverse the array and keep updating the prefix sum.
3. For each prefix sum, check how many times `(sum - k)` exists in the multiset.
4. Add that count to the answer.
5. Insert the current prefix sum into the multiset.

---

## C++ Solution

```cpp
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_multiset<int> fap;  
        int sum = 0;
        int count = 0;

        // Base case to handle subarrays starting from index 0
        fap.insert(0);

        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];

            // Count occurrences of (sum - k)
            if (fap.count(sum - k)) {
                count += fap.count(sum - k);
            }

            // Store current prefix sum
            fap.insert(sum);
        }

        return count;
    }
};
```

## Complexity Analysis
- Time Complexity: O(n)
- Space Complexity: O(n)
