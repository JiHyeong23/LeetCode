class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sols = {}
        for i in range(len(mat)):
            sol = mat[i].count(1)
            sols[i] = sol

        sols = sorted(sols.items(), key=lambda item:item[1])

        answer = []
        for i in range(k):
            answer.append(sols[i][0])
        
        return answer