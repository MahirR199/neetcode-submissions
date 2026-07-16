class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        for i in range(0,len(strs)):
            added = False
            for storingList in output:
                if len(storingList) != 0:
                    if self.anagram(storingList[0], strs[i]):
                        storingList.append(strs[i])
                        added = True
                        break
            if not added:
                output.append([strs[i]])
        return output

    def anagram(self, s: str, t: str) -> bool:
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
