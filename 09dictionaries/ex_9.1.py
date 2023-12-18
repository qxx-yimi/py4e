name = input("Enter file:")
handle = open(name)
max_email, max_count = '', 0
word_c = {}
for line in handle:
    if line.startswith('From '):
        email = line.split()[1]
        word_c[email] = word_c.get(email, 0) + 1
        if word_c[email] > max_count:
            max_email, max_count = email, word_c[email]

print(max_email, max_count)
