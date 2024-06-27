def twoSum_two_passes(nums, target):
    numMap = {}
    for i, num in enumerate(nums):
        numMap[num] = i
    for i, num in enumerate(nums):
        complement = target - num
        if complement in numMap and numMap[complement] != i:
            print()
            return [i, numMap[complement]]
    return []


print(twoSum_two_passes([1, 2, 4, 6], 8))


def twoSum_one_pass(nums, target):
    numMap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in numMap:
            return [numMap[complement], i]
        numMap[num] = i
    return []

print(twoSum_one_pass([1, 2, 4, 6], 8))

