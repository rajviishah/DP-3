'''
Approach:
1. use counter to count the number of values
2. make a new list with values*counter = total points
3. this new list is the nums of house robber
4. here take 0 points for the values which are not present thus, this will be house robber problem
TC: O(n)
SC: O(n)
'''


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(lambda: 0)
        max_number = max(nums)
        points = Counter(nums)

        max_points = [0] * (max_number + 2)
        for num in range(len(max_points)):
            max_points[num] = max(max_points[num - 1], max_points[num - 2] + points[num] * num)

        return max_points[max_number]

