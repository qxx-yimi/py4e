text = "X-DSPAM-Confidence:    0.8475"
s = text.find('0')
print(float(text[s:]))
