from collections import defaultdict
from itertools import product
from bisect import bisect_left

def solution(info, query):
    score_map = defaultdict(list)

    for person in info:
        data = person.split()
        conditions = data[:4]
        score = int(data[4])

        for selected in product([False, True], repeat=4):
            key = tuple(
                value if use else "-"
                for value, use in zip(conditions, selected)
            )
            score_map[key].append(score)

    for scores in score_map.values():
        scores.sort()

    answer = []

    for q in query:
        data = q.replace(" and ", " ").split()
        key = tuple(data[:4])
        target = int(data[4])

        scores = score_map.get(key, [])
        idx = bisect_left(scores, target)

        answer.append(len(scores) - idx)

    return answer