import time


def profiler_sum_while(nums: list) -> None:
    """Профилируем сложение элементов через цикл while"""
    start = time.perf_counter()
    nums_sum = 0
    i = 0
    while i < len(nums):
        nums_sum += nums[i]
        i += 1
    finish = time.perf_counter()
    print(nums_sum, finish - start, 'while')


def profiler_sum_for_in(nums: list) -> None:
    """Профилируем сложение элементов через цикл for"""
    start = time.perf_counter()
    nums_sum = 0
    for num in nums:
        nums_sum += num
    finish = time.perf_counter()
    print(nums_sum, finish - start, 'for in')


if __name__ == '__main__':
    nums = []
    for num in range(1, 10 ** 6 + 1):
        nums.append(num)

    profiler_sum_while(nums)
    profiler_sum_for_in(nums)



