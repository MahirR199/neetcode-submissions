class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        resList = [0]*len(temperatures)
        resList[len(temperatures)-1] = 0
        for i in range(1, len(temperatures)):
            idx = len(temperatures) - 1 - i
            if (temperatures[idx]<temperatures[idx+1]):
                resList[idx] = 1
            else:
                for j in range(idx+1 + resList[idx+1], len(temperatures)):
                    if (temperatures[idx]<temperatures[j]):
                        resList[idx] = j-idx
                        break
                    if j == len(temperatures)-1:
                        resList[idx] = 0 
        return resList


