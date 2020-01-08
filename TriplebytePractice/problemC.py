# input
# min sequence length
k = int(input())

# entire sequence data
filter_results = list(input())
filter_results = list(map(int, filter_results))


# desired ouput
# f = 1 based index of first element of subsequence
# l = length of subsequence

# try divide and conquer approach
# note subsequence is contiguous
def findSuccessRate(sequence):
    count = 0
    for num in sequence:
        if num != 0:
            count += 1
    return count / len(sequence)

f = 0
l = k
rate = 0
for index in range(len(filter_results)):
    if len(filter_results) - index < k:
        break
    for i in range(index + k, len(filter_results) + 1):
        current_rate = findSuccessRate(filter_results[index:i])
        if current_rate > rate:
            rate = current_rate
            f = index + 1
            l = i - index

print(str(f) + ' ' + str(l))
