# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count, result = 0, 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    num = float(line[line.find('0'):])
    result += num
print("Average spam confidence:",result/count)
