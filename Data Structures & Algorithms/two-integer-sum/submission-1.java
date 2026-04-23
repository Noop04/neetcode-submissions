class Solution {
    public int[] twoSum(int[] nums, int target) {
        /* loop thru nums with a map 
        *target - i if this int is in map then return current index and 
        * the other*/
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(target - nums[i])) {
                return new int[]{map.get(target - nums[i]), i};
            }
            else {
                map.put(nums[i], i);
            }
        }
        return new int[]{};
    }
}
