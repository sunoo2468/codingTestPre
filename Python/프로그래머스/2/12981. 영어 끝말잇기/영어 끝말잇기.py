def solution(n, words):
    answer = []
    used_words = set()
    
    i = 0
    for _ in range(len(words)):
        if(words[i] in used_words):
            return [i % n + 1, i // n + 1]
        used_words.append(words[i])
        if(i != 0 and used_words[i-1][-1] != used_words[i][0]):
            return [i % n + 1, i // n + 1]
        i += 1
            
    return [0, 0]

def solution(n, words):
    used_words = set()

    for i in range(len(words)):

        # 이미 나온 단어
        if words[i] in used_words:
            return [(i % n) + 1, (i // n) + 1]

        # 앞 단어의 마지막 글자와 연결되지 않음
        if i > 0 and words[i - 1][-1] != words[i][0]:
            return [(i % n) + 1, (i // n) + 1]

        used_words.add(words[i])

    return [0, 0]