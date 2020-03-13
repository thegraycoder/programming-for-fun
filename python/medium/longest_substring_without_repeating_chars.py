# Return the length of longest substring in the string
# abcabcbb => "abc" 3
# pwwkew => "wke" 3


def longest_substring_with_repeating_chars(string):
    # n is the length of string
    # i is the first pointer
    # j is the second pointer
    n, i, j, ans = len(string), 0, 0, 0
    hash_set = set()

    while j < n:
        if string[j] not in hash_set:
            hash_set.add(string[j])
            j += 1
            ans = max(ans, len(hash_set))
        else:
            hash_set.remove(string[i])
            i += 1
    return ans


print(longest_substring_with_repeating_chars("abcabcbb"))
print(longest_substring_with_repeating_chars("bbbbbbb"))
print(longest_substring_with_repeating_chars("pwwkew"))
