class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
            # Find the shortest string in the array
        min_length = min(len(s) for s in strs)
        result = ""
    
        # Iterate over characters up to the length of the shortest string
        for i in range(min_length):
            # Get the character at the current index from the first string
            char = strs[0][i]
    
            # Check if the character is present at the same index in all other strings
            if all(s[i] == char for s in strs):
                result += char
            else:
                break
    
        return result

solution = Solution()
print(solution.longestCommonPrefix(['flower','flow','flight']))
