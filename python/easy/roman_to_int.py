# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together.
# Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
# Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
#
# Example 1:
#
# Input: "III"
# Output: 3
# Example 2:
#
# Input: "IV"
# Output: 4
# Example 3:
#
# Input: "IX"
# Output: 9
# Example 4:
#
# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 5:
#
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


def roman_to_int(s: str) -> int:
    roman_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    answer = 0
    length = len(s)
    visited = [0]*length
    for i in range(length):
        if visited[i] == 1:
            continue
        if s[i] in ['I', 'X', 'C'] and i < length - 1:
            if s[i + 1] in ['V', 'X', 'L', 'C', 'D', 'M'] and roman_map[s[i+1]] > roman_map[s[i]]:
                answer += roman_map[s[i+1]] - roman_map[s[i]]
                visited[i+1] = 1
            else:
                answer += roman_map[s[i]]
        else:
            answer += roman_map[s[i]]
        visited[i] = 1
    return answer


roman_to_int('III')
roman_to_int('IV')
roman_to_int('IX')
roman_to_int('LVIII')
roman_to_int('MCMXCIV')
roman_to_int('DCXXI')
