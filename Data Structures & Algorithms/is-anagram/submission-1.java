class Solution {
    public boolean isAnagram(String s, String t) {
        /* check if lengths are not equal
        *  create hashmap loop thru s and add the char
        *  go thru t and subtract for every char val
        *  if char not in return false
        *  go thru map and check if values = 0*/
        if (s.length() != t.length()) return false;

        Map<Character, Integer> letters = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            if (!letters.containsKey(s.charAt(i))) { 
                letters.put(s.charAt(i), 1);
            } else {
                letters.replace(s.charAt(i), letters.get(s.charAt(i)) + 1);
            }
        }
        for (int i = 0; i < t.length(); i++) {
            if (!letters.containsKey(t.charAt(i))) return false;

            letters.replace(t.charAt(i), letters.get(t.charAt(i)) - 1);
        }

        for (Integer i : letters.values()) {
            if (i != 0) return false;
        }
        return true;
    }
}
