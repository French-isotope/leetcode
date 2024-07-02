import itertools

strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]
strs3 = ["a", "ab"]
strs4 = ["flower","flower","flower","flower"]


def longestCommonPrefix(strs):
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]

    strs.sort(key=len)
    shortest_str = strs[0]
    result = ""
    if shortest_str == "":
        return result

    for index_strs, letter in enumerate(shortest_str):
        for word in strs[1:]:
            if word == shortest_str:
                continue
            if index_strs == len(shortest_str):
                return shortest_str
            if word[index_strs] != letter:
                return shortest_str[:index_strs]
    return shortest_str


print(longestCommonPrefix(strs1))
print(longestCommonPrefix(strs2))
print(longestCommonPrefix(strs3))
print(longestCommonPrefix(strs4))

