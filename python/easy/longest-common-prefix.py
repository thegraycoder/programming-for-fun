# Write a function to find the longest common prefix string amongst an array of strings
# If there is no common prefix, return an empty string "".


def longest_common_prefix(strs):
    lcp = ''
    if not strs:
        return lcp
    minlen = len(strs[0])
    for string in strs:
        minlen = min(len(string), minlen)

    for i in range(minlen):
        char = strs[0][i]
        for string in strs:
            if string[i] != char:
                return lcp
        lcp += char
    return lcp


# Test cases
print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"]))
