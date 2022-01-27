import time

nums = []
for num in range(1, 10 ** 6 + 1):
    nums.append(num)

start = time.perf_counter()
# print(start)
nums_sum = 0
i = 0
while i < len(nums):
    nums_sum += nums[i]
    i += 1
finish = time.perf_counter()
# print(finish)
print(nums_sum, finish - start, 'while')

start = time.perf_counter()
# print(start)
nums_sum = 0
for num in nums:
    nums_sum += num
finish = time.perf_counter()
# print(finish)
print(nums_sum, finish - start, 'for in')
