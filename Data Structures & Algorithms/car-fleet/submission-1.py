class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Calculate time to reach target (n)
        #n = (target - position)/speed
        #if time to reach target is greater and position is greater, fleet becomes 1
        #if n1>=n2 and position1 >= position2 or n1<=n2 and position1 <= position2:
            #fleets-1
        #example 2 listN = [3, 4.5, 10, 3]
        pair = [(p, s) for p,s in zip(position, speed)]
        pair.sort(reverse = True)
        stack = []
        for p, s in pair:
            stack.append((target-p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]: #if speed is less or equal (fleets-=1)
                stack.pop()
        return len(stack)
                