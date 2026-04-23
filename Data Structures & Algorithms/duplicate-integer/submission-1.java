class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> ints = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (!ints.contains(nums[i])) {
                ints.add(nums[i]);
            } else {
                return true;
            }
        }
        return false;
    }
}
