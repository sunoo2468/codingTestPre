import java.util.Arrays;

class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        
        int[] first_size = new int [sizes.length];
        int[] second_size = new int [sizes.length];
        
        for(int i=0; i<sizes.length; i++){
            int big = Math.max(sizes[i][0], sizes[i][1]);
            int small = Math.min(sizes[i][0], sizes[i][1]);
            first_size[i]= big;
            second_size[i]=small;
        }
        
        Arrays.sort(first_size);
        Arrays.sort(second_size);
        
        answer = first_size[first_size.length - 1] * second_size[second_size.length - 1];
        
        return answer;
    }
}