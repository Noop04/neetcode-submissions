class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> numbers = new HashSet<>();
        for (int i : nums) {
            if (!numbers.contains(i)) numbers.add(i);
            else {return true; } // dup found
        }
        return false;
    }
}
