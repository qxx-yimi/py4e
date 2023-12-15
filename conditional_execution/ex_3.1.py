hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
rate = float(rate)
total = 0.0
if h <= 40:
    total = h * rate
else:
    total = 40 * rate + (h-40) * rate * 1.5
print(total)
