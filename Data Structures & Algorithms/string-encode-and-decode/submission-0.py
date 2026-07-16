class Solution:

    def encode(self, strs: List[str]) -> str:
        news = ""
        for string in strs:
            news += str(len(string)) + '}' + string
        return news
    def decode(self, s: str) -> List[str]:
        newL = []
        word = ""
        loop = ""
        while s != "":
            for c in s:
                if c != '}':
                    loop += c
                else:
                    break
            for i in range(int(loop)):
                word += (s[len(loop)+1+i])
            newL.append(word)
            word = ""
            s = s[len(loop)+1+int(loop):]
            loop = ""
        return newL
