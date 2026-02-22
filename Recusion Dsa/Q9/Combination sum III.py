class Solution:
    def combinationSum3(self, k: int, n: int):
        result = []
        
        def backtrack(start, path, total):
            # If length is k
            if len(path) == k:
                if total == n:
                    result.append(path[:])
                return
            
            # Try numbers from current start to 9
            for num in range(start, 10):
                
                # Pruning (important optimization)
                if total + num > n:
                    break
                
                path.append(num)
                backtrack(num + 1, path, total + num)
                path.pop()   # backtrack
        
        backtrack(1, [], 0)
        return result
