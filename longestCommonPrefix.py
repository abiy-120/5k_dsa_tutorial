def longestCommonPrefix(strs):
    common = ""
    strs.sort()
    nStrs = [strs[0], strs[-1]]
    nStrs.sort(key=len)
    for index, character in enumerate(nStrs[0]):
        if character == nStrs[1][index]:
            common += character
        else:
            return common
    return common
