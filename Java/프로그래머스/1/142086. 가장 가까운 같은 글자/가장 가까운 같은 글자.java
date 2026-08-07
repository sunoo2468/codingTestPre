import java.util.HashMap;

class Solution {
    //입력 데이터
    public int[] solution(String s) {

        int[] answer = new int[s.length()]; //s 길이만큼의 결과 리스트 반환

        HashMap<Character, Integer> map = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            
            if(map.containsKey(c)) {
                answer[i] = i - map.get(c);
            }
            else answer[i] = -1;
            
            map.put(c, i);
        }

        return answer;
    }
}