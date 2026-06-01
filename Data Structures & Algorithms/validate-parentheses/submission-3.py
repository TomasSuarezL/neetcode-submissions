class Solution:
    def isValid(self, s: str) -> bool:
        def isOpening(s: str)->bool:
            if s=='{' or s=='(' or s=='[':
                return True
            return False

        def isClosing(open_char: str, close_char: str)-> bool:
            if open_char == '{' and close_char == '}':
                return True
            elif open_char == '(' and close_char == ')':
                return True
            elif open_char == '[' and close_char == ']':
                return True
            return False

        last_idx = 0
        stack = []
        for char in s:
            print(stack, last_idx, char)
            if isOpening(char):
                stack.append(char)
                last_idx += 1
            elif last_idx < 1:
                return False
            elif isClosing(stack[last_idx-1], char):
                stack.pop()
                last_idx -= 1
            else:
                return False

        if len(stack)==0:
            return True 
        return False
