from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        n = len(nums)
        i = 0
        while i != n - 1:
            j = i + 1
            k = n - 1
            while j < n and j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    answer.append(sorted([nums[i], nums[j], nums[k]]))

                    while j != k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
                    while k != 0 and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    while k != 0 and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1

                else:
                    while j != k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1

            while i != n - 1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return answer


nums = list(map(int, input().split()))
Sol = Solution()
print(Sol.threeSum(nums))
