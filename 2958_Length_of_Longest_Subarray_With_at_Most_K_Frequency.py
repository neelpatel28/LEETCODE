class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = {}
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            # Add the current element to the frequency map
            count[nums[right]] = count.get(nums[right], 0) + 1
            
            # Shrink the window from the left if the frequency exceeds k
            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1
                
            # Update the maximum length found so far
            max_len = max(max_len, right - left + 1)
            
        return max_len
