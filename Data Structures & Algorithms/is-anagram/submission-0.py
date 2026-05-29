class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        for letter in s:
            count_s[letter] = 1 if count_s.get(letter) is None else count_s[letter] + 1
        
        count_t = {}
        for letter in t:
            count_t[letter] = 1 if count_t.get(letter) is None else count_t[letter] + 1

        if count_s == count_t:
            return True
        return False