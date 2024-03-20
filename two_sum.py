class Solution:
    def twoSum(self, nums, target):
        for i, num in enumerate(nums):
            print(i, num)
            complement = target - num
            if complement in nums[i+1:]:
                print(complement)
                if num == complement:
                    return [j for j,x in enumerate(nums) if x == complement]
                else:
                    return list([i, nums.index(complement)])
            else:
                continue

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
