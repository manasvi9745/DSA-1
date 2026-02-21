class Solution {
    public long repairCars(int[] ranks, int cars) {
        long low = 1;
        long high = 0;
        
        // Find maximum possible time
        int maxRank = 0;
        for (int r : ranks) {
            maxRank = Math.max(maxRank, r);
        }
        
        high = (long) maxRank * cars * cars;
        
        long ans = high;
        
        while (low <= high) {
            long mid = low + (high - low) / 2;
            
            if (canRepair(ranks, cars, mid)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        
        return ans;
    }
    
    private boolean canRepair(int[] ranks, int cars, long time) {
        long total = 0;
        
        for (int r : ranks) {
            total += (long) Math.sqrt(time / r);
            if (total >= cars) return true;
        }
        
        return false;
    }
}
