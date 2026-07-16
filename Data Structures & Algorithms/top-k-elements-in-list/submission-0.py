class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        freq = [[] for i in range(len(nums)+1)] #create a list of lists of n+1 elements

        for num in nums:
            d[num] = 1+d.get(num,0)
        for num, count in d.items():
            freq[count].append(num) #we created n+1 empty lists so if there was a freq of n it would have the index n and fit 
            #append so if there are ties u dont overwrite
        res = []
        for i in range(len(freq)-1, 0, -1): #go backwards and put it the most frequent elements
            for num in freq[i]:
                res.append(num)
                if len(res) == k: #when u reach len of k break and return
                    return res        
        