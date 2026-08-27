class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        # Check every number
        for num in num_set:
            # Only start counting if num is the beginning of a sequence
            if (num - 1) not in num_set:
                current = num
                length = 1

                # Keep checking the next number
                while (current + 1) in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest