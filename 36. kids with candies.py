def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)
    result = [(candy + extraCandies) >= max_candies for candy in candies]
    return result

candies = [2, 3, 5, 1, 3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))  # Output: [true, true, true, false, true]

candies = [4, 2, 1, 1, 2]
extraCandies = 1
print(kidsWithCandies(candies, extraCandies))  # Output: [true, false, false, false, falsecandies = [12, 1, 12]
extraCandies = 10
print(kidsWithCandies(candies, extraCandies))  # Output: [true, false, true]

#Time complexity:O(n)
#Space complexity:O(n)
