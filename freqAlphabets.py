def freqAlphabets(s):
    letterMap = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    l = []
    for i, c in enumerate(s):
        if c == "#":
            l.pop()
            l.pop()
            l.append(s[i-2:i+1])
            continue
        l.append(c)
    result = ""
    for d in l:
        if len(d) > 1:
            result += letterMap[int(d[0:2])-1]
        else:
            result += letterMap[int(d)-1]
    return result
