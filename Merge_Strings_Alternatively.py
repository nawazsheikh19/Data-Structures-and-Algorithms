You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

word1 = "abc"
word2 = "pqr"
output = "apbqcr"

def mergeAlternately(word1, word2):
        n1 = len(word1)
        n2 = len(word2)

        i = 0
        j = 0

        output = ''

        while i < n1 or j < n2:
            if i < n1:
                output = output + word1[i]
                i = i + 1
            if j < n2:
                output = output + word2[j]
                j = j + 1
        return output

result = mergeAlternately(word1, word2)
print(result)
