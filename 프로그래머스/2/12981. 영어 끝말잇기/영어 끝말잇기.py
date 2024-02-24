def solution(n, words):
    used_words = []
    number, order = 0,0

    used_words.append(words[0])
    last_word = words[0][-1]
    for i in range(1,len(words)):
        if words[i] not in used_words and words[i][0] == last_word:
            used_words.append(words[i])
            last_word = words[i][-1]
        else:
            number = (i%n)+1
            order = (i//n)+1
            break
    
    return [number, order]