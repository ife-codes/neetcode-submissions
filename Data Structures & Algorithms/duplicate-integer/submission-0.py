class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst = []
        if 0 <= len(nums) <= (10 ** 5):
            for num in nums:
                if (-(10 ** 9)) <= num <= (10 ** 9):
                    if num in lst:
                        return True
                        break
                    lst.append(num)
                 
            return False
        return False

