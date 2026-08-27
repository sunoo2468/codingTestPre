class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        String result = "";
        
        for(int i=0; i<n; i++){
            result = Integer.toBinaryString(arr1[i] | arr2[i]);
            result = String.format("%" + n + "s", result);
            
            result = result.replace("1", "#");
            result = result.replace("0", " ");
            
            answer[i] = result;
        }
        
        return answer;
    }
}