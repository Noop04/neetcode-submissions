class Solution {
    public boolean isAnagram(String s, String t) {
      Map<Character, Integer> count = new HashMap<>();
      // Go through s and add the values and keys
      // go through t subtraxt the values 
      // if a key does not exist return false
      // go through each key of count and check if vals = 0 => true
      if (s.length() == 0 || t.length() == 0) return false;

      for (int i = 0; i < s.length(); i++) {
        if (!count.containsKey(s.charAt(i))) {
            count.put(s.charAt(i), 1);
        } else {
            count.replace(s.charAt(i), count.get(s.charAt(i)) + 1);
        }
      }
      for (int i = 0; i < t.length(); i++) {
        if (!count.containsKey(t.charAt(i))) return false;
        count.replace(t.charAt(i), count.get(t.charAt(i)) - 1);
      }
      for (Integer i : count.values()) {
        if (i != 0) return false;
      }
      return true;
    }
}
