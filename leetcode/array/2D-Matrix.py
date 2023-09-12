from typing import List


class Solution:
    def bin_search(self, arr, target):
        left = 0
        right = len(arr)-1
        while left <= right:
            ptr = (right + left) // 2
            if target > arr[ptr]:
                left = ptr + 1
            elif target == arr[ptr]:
                return ptr
            elif target < arr[left]:
                return left
            else:
                right = ptr - 1
        return left


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        last_elements = []
        for i in range(len(matrix)):
            last_elements.append(matrix[i][len(matrix[i]) - 1])

        ans_row = self.bin_search(last_elements, target)
        if ans_row > len(matrix) - 1:
            return False
        else:
            ans_col = self.bin_search(matrix[ans_row], target)
        if matrix[ans_row][ans_col] == target:
            return True
        else:
            return False

sol = Solution()
matrix = [[1]]
target = 2
print(sol.searchMatrix(matrix, target))
