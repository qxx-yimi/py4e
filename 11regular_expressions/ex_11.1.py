import re
filename = 'regex_sum_1940213.txt'
handle = open(filename)
text = handle.read()
nums = re.findall('[0-9]+', text)
nums = list(map(int, nums))
print(sum(nums))
