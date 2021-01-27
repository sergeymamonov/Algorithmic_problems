def two_sum(nums, target: int):
    viewed_numbers = {}
    for index, number in enumerate(nums):
        difference = target - number
        if difference not in viewed_numbers:
            viewed_numbers[number] = index
        else:
            return [viewed_numbers[difference], index]


print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum([3, 2, 4], 6))  # [1, 2]
print(two_sum([3, 3], 6))  # [0, 1]
