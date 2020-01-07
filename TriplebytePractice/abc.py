# input
# first line is numbers
nums = input().split(' ')
nums = list(map(int, nums))
nums.sort()

# second line is ABC combo
abc = list(input())

output = []
for letter in abc:
    if letter == 'C':
        output.append(nums[2])
    elif letter == 'B':
        output.append(nums[1])
    else:
        output.append(nums[0])

output = list(map(str, output))
print(' '.join(output))