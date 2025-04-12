def similarPairs(words: list[str]) -> int:
    words = [set(x) for x in words]
    count = 0
    for index, word in enumerate(words):
        count += words[index+1:].count(word)
    return count
