# Write a function to find the longest common prefix string amongst an array of strings
# If there is no common prefix, return an empty string "".


# Runtime: 28 ms
# Approach 1: Length LCP cannot be greater than that of smallest string
# Calculate min length O(n)
# While len(LCP) < minlen build prefix and return if char do not match
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


# Runtime 48 ms
# Approach 2: Build a trie with word count and search for nodes with
# word count equal to length of array strs (i.e. nodes common in all strings)
class TrieNode:
    def __init__(self):
        self.val = ''
        self.word_count = 0
        self.children = []

    def search_node_with_word_count(self, wc):
        for node in self.children:
            if node.word_count == wc:
                return node


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, string):
        last_node = self.root
        for char in string:
            found = False
            for node in last_node.children:
                if node.val == char:
                    node.word_count += 1
                    found = True
                    last_node = node
            if not found:
                node = TrieNode()
                node.val = char
                node.word_count = 1
                last_node.children.append(node)
                last_node = node

    def find_common_prefix(self, length):
        lcp = ''
        last_node = self.root
        while last_node:
            node = last_node.search_node_with_word_count(length)
            if node:
                lcp += node.val
            last_node = node
        return lcp


# Test cases
test_cases = [
    ["dog", "racecar", "car"],
    ["flower", "flow", "flight"],
    ["apple", "apples", "apps", "ape"]
]
for arr in test_cases:
    trie = Trie()
    for s in arr:
        trie.insert(s)
    max_word_count = len(arr)
    print(trie.find_common_prefix(length=max_word_count))
