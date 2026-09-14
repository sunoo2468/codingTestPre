def solution(name, yearning, photo):
    answer = []

    # 이름 : 추억 점수
    score = {}

    for i in range(len(name)):
        score[name[i]] = yearning[i]

    # 사진 한 장씩 확인
    for people in photo:
        total = 0

        for person in people:
            if person in score:
                total += score[person]

        answer.append(total)

    return answer