
def nextGreaterElements(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    stack = []
    greater = [None] * len(nums)

    for i in range(2 * len(nums)):
        temp = nums[i % len(nums)]
        while stack and stack[-1][1] < temp:
            greater[stack[-1][0]] = temp
            stack.pop()
        if greater[i % len(nums)] == None:
            stack.append((i % len(nums), temp))

    while stack:
        greater[stack[-1][0]] = -1
        stack.pop()
    return greater

test = [1, 2, 1]
nextGreaterElements(test)
