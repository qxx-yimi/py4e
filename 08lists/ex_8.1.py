fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line_s = line.split()
    for word in line_s:
        if word not in lst:
            lst.append(word)

lst.sort()
print(lst)
