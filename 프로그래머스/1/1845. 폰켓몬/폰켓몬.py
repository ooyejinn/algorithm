def solution(nums):
    half_n = len(nums) // 2

    unique_ponkemons = set(nums)
    num_of_types = len(unique_ponkemons)

    return min(half_n, num_of_types)