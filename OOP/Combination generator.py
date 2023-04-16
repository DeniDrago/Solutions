from itertools import permutations


def permutations_generator(nums):
    for perm in permutations(nums):
        yield perm


if __name__ == '__main__':
    for permutation in permutations_generator([1, 2, 3]):
        print(permutation)
