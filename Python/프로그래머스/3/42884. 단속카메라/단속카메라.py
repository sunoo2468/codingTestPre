def solution(routes):
    answer = 1

    routes.sort(key=lambda x: x[1])

    state = routes[0][1]

    for i in range(1, len(routes)):
        if state < routes[i][0]:
            state = routes[i][1]
            answer += 1

    return answer