class Solution(object):
    def generateString(self, str1, str2):
        n, m = len(str1), len(str2)
        L = n + m - 1

        word = ['?'] * L
        locked = [False] * L  # marks positions fixed by 'T'

        # Step 1: Apply 'T' constraints
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if word[i + j] == '?' or word[i + j] == str2[j]:
                        word[i + j] = str2[j]
                        locked[i + j] = True
                    else:
                        return ""

        # Step 2: Fill remaining with 'a'
        for i in range(L):
            if word[i] == '?':
                word[i] = 'a'

        # Step 3: Handle 'F'
        for i in range(n):
            if str1[i] == 'F':
                if ''.join(word[i:i+m]) == str2:
                    # Need to break match
                    broken = False

                    for j in range(m - 1, -1, -1):  # rightmost first
                        pos = i + j

                        if locked[pos]:
                            continue  # cannot change

                        original = word[pos]

                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            if c != str2[j]:
                                word[pos] = c
                                broken = True
                                break

                        if broken:
                            break
                        else:
                            word[pos] = original

                    if not broken:
                        return ""

        return ''.join(word)