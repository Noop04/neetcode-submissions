class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> topk = new HashMap<>();
        for (int i : nums) {
            if (!topk.containsKey(i)) {
                topk.put(i, 1);
            } else {
                topk.put(i, topk.get(i) + 1);
            }
        }

       int[] topKeys = new int[k];

        List<Map.Entry<Integer, Integer>> entries = new ArrayList<>(topk.entrySet());
        entries.sort((a, b) -> b.getValue() - a.getValue());

        for (int i = 0; i < k; i++) {
            topKeys[i] = entries.get(i).getKey();
        }

        return topKeys;
    }
}
