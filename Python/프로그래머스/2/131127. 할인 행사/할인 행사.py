def solution(want, number, discount):
    answer = 0
    want_dict = {}

    for i in range(len(want)):
        want_dict[want[i]] = number[i]

    window = {}

    for item in discount[:10]:
        if item in window:
            window[item] += 1
        else:
            window[item] = 1

    # 첫 번째 10일 확인
    if window == want_dict:
        answer += 1

    for i in range(10, len(discount)):

        out_item = discount[i - 10]
        window[out_item] -= 1

        if window[out_item] == 0:
            del window[out_item]

        in_item = discount[i]

        if in_item in window:
            window[in_item] += 1
        else:
            window[in_item] = 1

        if window == want_dict:
            answer += 1

    return answer