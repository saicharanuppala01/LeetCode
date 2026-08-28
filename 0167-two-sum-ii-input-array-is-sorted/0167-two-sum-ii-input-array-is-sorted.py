class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n - 1
        while (left < right):
            temp_sum=0
            temp_sum=numbers[left]+numbers[right]
            if temp_sum == target:
                return [left+1,right+1]
            elif temp_sum < target:
                left+=1
            else:
                right-=1
        return []