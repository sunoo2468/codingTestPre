import java.util.*;

class Solution {
    public int solution(String[][] clothes) {

        HashMap<String, Integer> map = new HashMap<>();

        // 옷 종류별 개수 계산
        for (int i = 0; i < clothes.length; i++) {

            String type = clothes[i][1];

            map.put(type, map.getOrDefault(type, 0) + 1);
        }

        // 경우의 수는 곱셈이므로 1부터 시작
        int answer = 1;

        // 종류별 옷 개수를 하나씩 가져옴
        for (int count : map.values()) {

            // 해당 종류를 착용하지 않는 경우까지 포함
            answer *= (count + 1);
        }

        // 아무것도 착용하지 않는 경우 제외
        return answer - 1;
    }
}