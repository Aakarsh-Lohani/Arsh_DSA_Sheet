# https://leetcode.com/problems/wildcard-matching/description/
# 44. Wildcard Matching

#Beats 88%
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Initialize the pointers for the input string and the pattern
        i = 0
        j = 0
    
        # Initialize the pointers for the last character matched and the last
        # '*' encountered in the pattern
        last_match = 0
        star = -1
    
        # Loop through the input string and the pattern
        while i < len(s):
            # Check if the current characters in the input string and the pattern
            # match, or if the pattern character is a '?'
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                # Move the pointers for the input string and the pattern forward
                i += 1
                j += 1
            # Check if the current pattern character is a '*'
            elif j < len(p) and p[j] == '*':
                # Store the current positions of the pointers for the input string
                # and the pattern
                last_match = i
                star = j
                # Move the pointer for the pattern forward
                j += 1
            # If none of the above conditions are met, check if we have encountered
            # a '*' in the pattern previously
            elif star != -1:
                # Move the pointer for the pattern back to the last '*'
                j = star + 1
                # Move the pointer for the input string to the next character
                # after the last character matched
                i = last_match + 1
                # Move the pointer for the last character matched forward
                last_match += 1
            # If none of the above conditions are met, the input string and the
            # pattern do not match
            else:
                return False
    
        # Loop through the remaining characters in the pattern and check if they
        # are all '*' characters
        while j < len(p) and p[j] == '*':
            j += 1
    
        # Return True if all the characters in the pattern have been processed,
        # False otherwise
        return j == len(p)
    

# Beats 37%
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True

        for j in range(1, len(p) + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == '?' or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]

        return dp[len(s)][len(p)]