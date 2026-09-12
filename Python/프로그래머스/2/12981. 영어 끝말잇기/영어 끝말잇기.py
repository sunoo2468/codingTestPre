def solution(n, words):
    answer = []
    used_words = []
    
    i = 0
    for _ in range(len(words)):
        if(words[i] in used_words):
            return [i % n + 1, i // n + 1]
        used_words.append(words[i])
        if(i != 0 and used_words[i-1][-1] != used_words[i][0]):
            return [i % n + 1, i // n + 1]
        i += 1
            
    return [0, 0]