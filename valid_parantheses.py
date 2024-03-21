class Solution:
    def isValid(self, s):
        my_chars = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                # Ignoring any other characters
                continue
        
        return len(stack) == 0

solution = Solution()
print(solution.isValid('(){}[]'))
