import java.util.Arrays;

class Solution {
    public String solution(int[] numbers) {

        String[] nums = new String[numbers.length];
        StringBuilder sb = new StringBuilder();

    for (int i = 0; i < numbers.length; i++) {
        nums[i] = String.valueOf(numbers[i]);
    }
        
    Arrays.sort(nums, (a, b) -> {
        String ab = a + b; // a가 앞에 오는 경우
        String ba = b + a; // b가 앞에 오는 경우

        // 두 경우를 비교해서 더 큰 숫자를 만드는 순서가 앞으로 오도록 정렬
        return ba.compareTo(ab);
    });
        
    if (nums[0].equals("0")) {
        return "0";
    }

    for (String num : nums) {
        sb.append(num);
    }

    return sb.toString();
        
    }
}