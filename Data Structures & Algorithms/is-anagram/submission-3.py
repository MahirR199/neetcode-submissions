class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        for l in s:
            if l in a:
                a[l] += 1
            else:
                a[l] = 1
        
        for l in t:
            if l in a:
                a[l] -= 1
            else:
                return False
        
        for chars in a.values():
            if chars != 0:
                return False
        return True
