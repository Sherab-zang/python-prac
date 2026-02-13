# Longest Increasing Streak

def longest_increasing_streak(nums):
    if not nums:
        return 0

    current_streak = 1
    max_streak = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            current_streak += 1
        else:
            current_streak = 1

        if current_streak > max_streak:
            max_streak = current_streak

    return max_streak


# test
print(longest_increasing_streak([1, 2, 3, 5, 6, 7, 8, 2]))
