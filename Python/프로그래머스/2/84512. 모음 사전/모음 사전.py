def solution(word):
    vowels = "AEIOU"
    weights = [781, 156, 31, 6, 1]

    answer = 0

    for i, char in enumerate(word):
        answer += vowels.index(char) * weights[i] + 1

    return answer