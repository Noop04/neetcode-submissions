class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Integer> seen = new HashMap<>();
        int i = 0;
        for (int num : nums) {
            if (!seen.containsKey(num)) {
                seen.put(num, i);
                i++;
            }
            else{ 
                return true;
            }
        }
    return false;
    }
}
