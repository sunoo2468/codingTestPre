import java.util.*; 
class Solution { 
    public int[] solution(int[] progresses, int[] speeds) { 
        Queue<Integer> queue = new LinkedList<>(); 
        List<Integer> result = new ArrayList<>(); 
        
        // 각 기능이 완료되기까지 걸리는 일수 계산 
        for (int i = 0; i < progresses.length; i++) { 
            int days = (int) Math.ceil( 
                (double) (100 - progresses[i]) / speeds[i] ); 
            queue.offer(days); 
        } 
        
        // Queue가 빌 때까지 배포 묶음 처리 
        while (!queue.isEmpty()) { 
            // 현재 배포 묶음의 기준이 되는 기능 
            int releaseDay = queue.poll(); 
            // 기준 기능 자체도 배포되므로 1부터 시작 
            int count = 1; 
            // 뒤의 기능이 기준 기능보다 빠르거나 같은 날 완료되면 함께 배포 
            while (!queue.isEmpty() && queue.peek() <= releaseDay) { 
                queue.poll(); count++; 
            } 
            // 이번 배포 묶음의 기능 개수 저장 
            result.add(count); 
        } 
        
        // List<Integer>를 int[]로 변환 
        int[] answer = new int[result.size()]; 
        for (int i = 0; i < result.size(); i++) { 
            answer[i] = result.get(i); 
        } 
        
        return answer; 
    } 
}