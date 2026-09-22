def solution(record):
    answer = []
    user_dict = {}
    history = []

    #1. 일단 split해서 각 act별 데이터를 저장
    for data in record:
        data = data.split()

        state = data[0]
        user_id = data[1]

        # 2. State에 따라 분기 타기
        if state == "Enter":
            nickname = data[2]

            user_dict[user_id] = nickname
            history.append([state, user_id])

        elif state == "Leave":
            history.append([state, user_id])

        elif state == "Change":
            nickname = data[2]

            user_dict[user_id] = nickname

    # 3. 최종 결과 정리
    for state, user_id in history:

        if state == "Enter":
            answer.append(user_dict[user_id] + "님이 들어왔습니다.")

        elif state == "Leave":
            answer.append(user_dict[user_id] + "님이 나갔습니다.")

    return answer