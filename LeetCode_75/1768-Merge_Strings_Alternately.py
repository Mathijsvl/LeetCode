class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = []
        i, j = 0, 0
        
        while i < len(word1) and j < len(word2):
            merged_string.append(word1[i])
            merged_string.append(word2[j])
            i += 1
            j += 1
        
        # Append remaining characters from the longer string
        if i < len(word1):
            merged_string.append(word1[i:]) # Create a substring starting from the index i to the end of the string
        if j < len(word2):
            merged_string.append(word2[j:]) # Create a substring starting from the index i to the end of the string
        
        return ''.join(merged_string)

# Create an instance of the Solution class
solution = Solution()

# Testcases
word1 = "abc"
word2 = "pqr"
print(solution.mergeAlternately(word1, word2))  # Output: "apbqcr"

word1 = "ab"
word2 = "pqrs"
print(solution.mergeAlternately(word1, word2))  # Output: "apbqrs"

word1 = "abcd"
word2 = "pq"
print(solution.mergeAlternately(word1, word2))  # Output: "apbqcd"