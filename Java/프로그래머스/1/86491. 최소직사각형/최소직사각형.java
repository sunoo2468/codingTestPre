class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        
        int maxBig=0;
        int maxSmall=0;
        
        for(int i=0; i<sizes.length; i++){
            int big = Math.max(sizes[i][0], sizes[i][1]);
            int small = Math.min(sizes[i][0], sizes[i][1]);
            
            maxBig = Math.max(maxBig, big);
            maxSmall = Math.max(maxSmall, small);
        }
        
        answer = maxBig * maxSmall;
        
        return answer;
    }
}