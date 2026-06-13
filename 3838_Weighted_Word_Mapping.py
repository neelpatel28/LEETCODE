class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        result_chars = []
        for word in words:
            total = 0
            for ch in word:
                total += weights[ord(ch) - ord('a')]
            mapped = chr(ord('z') - (total % 26))
            result_chars.append(mapped)
        return ''.join(result_chars)


if __name__ == "__main__":
    sol = Solution()
    print(sol.mapWordWeights(["abcd", "def", "xyz"], [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]))  # rij
    print(sol.mapWordWeights(["a", "b", "c"], [1] * 26))  # yyy
    print(sol.mapWordWeights(["abcd"], [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]))  # g
