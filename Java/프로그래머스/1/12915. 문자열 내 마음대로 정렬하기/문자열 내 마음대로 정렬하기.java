import java.util.Arrays;

class Solution {
    public String[] solution(String[] strings, int n) {

        Arrays.sort(strings, (a, b) -> {

            char charA = a.charAt(n);
            char charB = b.charAt(n);

            if (charA == charB) {
                return a.compareTo(b);
            }

            return charA - charB;
        });

        return strings;
    }
}