class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start_m = 0
        start_n = 0
        end_m = len(matrix)
        end_n = len(matrix[0])
        while start_m < end_m:
            mid_m = start_m + ((end_m-start_m)//2)
            if target < matrix[mid_m][0]:
                end_m = mid_m
            elif target > matrix[mid_m][0]:
                if target <= matrix[mid_m][end_n-1]:
                    start_m = mid_m
                    break
                else:
                    start_m = mid_m+1
            else:
                break
        while start_n < end_n:
            mid_n = start_n + ((end_n-start_n)//2)
            if target<matrix[mid_m][mid_n]:
                end_n = mid_n
            elif target>matrix[mid_m][mid_n]:
                start_n = mid_n+1
            else: 
                return True
        if start_n==end_n and target==matrix[mid_m][start_n-1]:
            return True
        return False


            