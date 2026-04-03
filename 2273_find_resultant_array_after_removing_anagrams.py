class Solution(object):
    def removeAnagrams(self, words):
        result = []
        prev = ""
        for word in words:
            sorted_word = ''.join(sorted(word))
            if sorted_word != prev:
                result.append(word)
                prev = sorted_word

        return result
    
obj = Solution()
print(obj.removeAnagrams(["abbca","cbaba","bbcaa","dcdd","cddd"])) # Output: ["abbca","dcdd"], Explanation: The anagrams are "abbca", "cbaba", and "bbcaa". We keep "abbca" and remove the other two. The anagrams are "dcdd" and "cddd". We keep "dcdd" and remove "cddd".

print(obj.removeAnagrams(["abba","baba","bbaa","cd","cd"])) # Output: ["abba","cd"], Explanation: The anagrams are "abba", "baba", and "bbaa". We keep "abba" and remove the other two. The anagrams are "cd" and "cd". We keep the first "cd" and remove the second one.

print(obj.removeAnagrams(["a","b","c","d","e"])) # Output: ["a","b","c","d","e"], Explanation: There are no anagrams in this case. We keep all the words.

print(obj.removeAnagrams(["a","a","a","a","a"])) # Output: ["a"], Explanation: The anagrams are "a", "a", "a", "a", and "a". We keep the first "a" and remove the other four.