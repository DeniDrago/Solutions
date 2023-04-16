def palindrome(n):
    for num in range(1, n):
        if str(num) == str(num)[::-1]:
            yield num


for nums in palindrome(2000):
    print(nums)
