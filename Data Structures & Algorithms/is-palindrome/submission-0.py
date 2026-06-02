class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric_s = "".join(char.lower() for char in s if char.isalnum())
        return alphanumeric_s == alphanumeric_s[::-1]