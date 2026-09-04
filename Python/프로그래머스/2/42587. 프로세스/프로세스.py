from collections import deque

def solution(priorities, location):
    queue = deque(enumerate(priorities))
    count = 0

    while queue:
        index, priority = queue.popleft()

        # 나보다 우선순위가 높은 프로세스가 남아있다면
        if queue and priority < max(p for i, p in queue):
            queue.append((index, priority))

        # 내가 현재 가장 높은 우선순위라면 실행
        else:
            count += 1

            # 실행된 프로세스가 내가 찾던 프로세스라면
            if index == location:
                return count