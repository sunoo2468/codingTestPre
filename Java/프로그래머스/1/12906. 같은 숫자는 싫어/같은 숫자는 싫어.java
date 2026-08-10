import java.util.*;

public class Solution {
    public int[] solution(int[] arr) { // 반환값 int[]
        
        // 배열리스트로 담아, 리스트의 값을 미정의로 두기
        // add를 얼마나 할지 모르기 때문
        ArrayList<Integer> list = new ArrayList<>();

        list.add(arr[0]); //무조건 첫번째 원소는 추가

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] != arr[i - 1]) {
                list.add(arr[i]);
            }
        }

        // int[]로 변환
        int[] answer = new int[list.size()];
        
        for (int i=0; i<list.size(); i++){
            answer[i] = list.get(i); //리스트에서 값 가져오기 =get()
        }
        
        return answer;
    }
}