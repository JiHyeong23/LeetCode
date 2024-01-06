class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        len1 = len(word1)
        len2 = len(word2)
        if len1 == len2:
            for i in range(len1):
                answer += word1[i]
                answer += word2[i]
        else:
            if len1 > len2:
                for i in range(len2):
                    answer += word1[i]
                    answer += word2[i]
                answer += word1[len2:]
            else:
                for i in range(len1):
                    answer += word1[i]
                    answer += word2[i]
                answer += word2[len1:]
        return answer