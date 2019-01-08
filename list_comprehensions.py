nums = [1,2,3,4,5,6,7,8,9,10]
new_list = []
# learning how to work better with list comprehensions
# various examples

# moving the list into a new list
new_list = [n for n in nums]
print(new_list)
# [1,2,3,4,5,6,7,8,9,10]

# adding only even numbers to the list
new_list = [n for n in nums if n%2==0]
print(new_list)
# [2, 4, 6, 8, 10]

# adding only odd numbers to the list
new_list = [n for n in nums if n%2==1]
print(new_list)
# [1, 3, 5, 7, 9]

# adding the power of each number to the list
new_list = [n**n for n in nums]
print(new_list)
# [1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489, 10000000000]

# multiplying each number by 3 and adding to the list
new_list = [n*3 for n in nums]
print(new_list)
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# finding max of all numbers in list
new_list = max([n for n in nums])
print(new_list)
# 10

# calculating the sum of all numbers
new_list = sum([n for n in nums])
print(new_list)
# 55

# nested for loop
new_list = [f"{letter}, {num}" for letter in "abcd" for num in range(4)]
print(new_list)
# ['a, 0', 'a, 1', 'a, 2', 'a, 3', 'b, 0', 'b, 1', 'b, 2', 'b, 3', 'c, 0', 'c, 1', 'c, 2', 'c, 3', 'd, 0', 'd, 1', 'd, 2', 'd, 3']

#dictionary comprehension

name = ['Bruce', 'Logan', 'Peter']
hero = ['Batman', 'Wolverine', 'Spiderman']

new_dict = {name:hero for name, hero in zip(name, hero)}
print(new_dict)
# {'Bruce': 'Batman', 'Logan': 'Wolverine', 'Peter': 'Spiderman'}

# set comprehension
letter_list = ['a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'e', 'e', 'f', 'f', 'g']
set_up = sorted({l for l in letter_list})
print(set_up)
# ['a', 'b', 'c', 'd', 'e', 'f','g']
