from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        dial = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        dials = [dial[x] for x in digits]
        com = list(product(*dials))
        answer = [''.join(x) for x in com]
        return answer