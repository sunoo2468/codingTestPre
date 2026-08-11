import java.util.*;

class Solution {
    boolean solution(String s) {

        // '(' 문자를 저장할 Stack 생성
        Stack<Character> stack = new Stack<>();

        // 문자열 s를 char 배열로 바꾼 뒤,
        // 문자를 하나씩 꺼내서 c에 저장
        for (char c : s.toCharArray()) {

            // 현재 문자가 '('라면
            if (c == '(') {

                // 나중에 ')'와 짝을 맞추기 위해 Stack에 저장
                stack.push(c);

            } else { // 현재 문자가 ')'라면

                // ')'가 나왔는데 Stack이 비어있다면
                // 짝을 맞출 '('가 없다는 뜻
                // 예: ")("
                if (stack.isEmpty()) {
                    return false;
                }

                // 짝을 맞출 '('가 존재하므로
                // Stack에서 '(' 하나를 꺼내서 제거
                stack.pop();
            }
        }

        // 문자열을 전부 확인한 후에도
        // Stack에 '('가 남아있다면 짝을 못 찾은 것
        //
        // Stack이 비어있으면 → true
        // Stack에 '('가 남아있으면 → false
        return stack.isEmpty();
    }
}