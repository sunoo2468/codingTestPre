import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {

        // commands의 개수만큼 정답 배열 생성
        int[] answer = new int[commands.length];

        for (int i = 0; i < commands.length; i++) {

            // 시작 위치, 끝 위치, 몇 번째 숫자인지 가져오기
            int start = commands[i][0];
            int end = commands[i][1];
            int k = commands[i][2];

            // 원본 배열에서 start번째 ~ end번째까지 복사
            int[] sliced = Arrays.copyOfRange(
                array,
                start - 1,
                end
            );

            // 잘라낸 배열 오름차순 정렬
            Arrays.sort(sliced);

            // 정렬된 배열의 k번째 값을 정답에 저장
            answer[i] = sliced[k - 1];
        }

        return answer;
    }
}