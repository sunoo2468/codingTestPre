from itertools import permutations

def solution(k, dungeons):
    answer = 0

    # 가능한 모든 던전 순서
    for order in permutations(dungeons):
        fatigue = k
        # print(fatigue)
        count = 0

        # 현재 순서대로 던전 탐험
        for dungeon in order:
            if fatigue >= dungeon[0]:
                fatigue -= dungeon[1]
                count += 1
            else:
                break

        answer = max(answer, count)

    return answer