class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = {}
        for c in s:
            if c in l:
                l[c] += 1
            else:
                l[c] = 1
        for c in t:
            if c in l:
                l[c] -= 1
            else:
                return False
        for x in l:
            if l[x] != 0:
                return False

        return True