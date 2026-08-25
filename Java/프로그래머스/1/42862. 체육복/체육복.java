class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        
        int[] clothes = new int[n+1];
        for (int i = 1; i <= n; i++) {
            clothes[i] = 1;
        }
        
        for(int student : lost){
            clothes[student]--;
        }
        for(int student : reserve){
            clothes[student]++;
        }
        
        for (int i = 1; i <= n; i++) {
            if (clothes[i] == 2) {

                // 앞사람 우선
                if (i > 1 && clothes[i - 1] == 0) {
                    clothes[i]--;
                    clothes[i - 1]++;
                }

                // 앞사람이 필요 없으면 뒷사람 확인
                else if (i < n && clothes[i + 1] == 0) {
                    clothes[i]--;
                    clothes[i + 1]++;
                }
            }
        }
        
        for (int i = 1; i <= n; i++) {
            if (clothes[i] >= 1) {
                answer++;
            }
        }
        return answer;
    }
}