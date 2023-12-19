name = input("Enter file:")
handle = open(name)
h_cnt = dict()

for line in handle:
    if not line.startswith('From '):
        continue
    colon = line.find(':')
    h = line[colon-2:colon]
    h_cnt[h] = h_cnt.get(h, 0) + 1

for k, v in sorted(h_cnt.items()):
    print(k,v)
