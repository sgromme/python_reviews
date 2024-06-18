from collections import ChainMap


nums = {"one":1, "two":2}
letters = {"a":"A", "b":"B"} 

nums_letters = ChainMap(nums, letters)

nums_letters


print(nums_letters["a"])

print("ChainMap")

arr = [1, 0, -5]

count = 0
