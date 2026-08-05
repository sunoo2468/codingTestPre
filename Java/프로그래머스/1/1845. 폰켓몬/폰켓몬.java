import java.util.HashSet;

class Solution {
    public int solution(int[] nums) {

        HashSet<Integer> set = new HashSet<>();

        for (int num : nums) {
            set.add(num);
        }

        int pick = nums.length / 2;
        int kind = set.size();

        return Math.min(pick, kind);
    }
}