from email.mime import base


base_10 = 231

# This is the number in binary: 11100111
print(f"This is the number in binary: {base_10:b}")

# This is the number in octal: 347
print(f"This is the number in octal: {base_10:o}")

# This is the number in hexadecimal: e7
print(f"This is the number in hexadecimal: {base_10:x}")

# This is the number in uppercase hexadecimal: E7
print(f"This is the number in uppercase hexadecimal: {base_10:X}")

print(50 * '-')

base_16 = int("E7", base=16)

# This is the number in decimal: 231
print(f"This is the number in decimal: {base_16:d}")
print(f"This is the number in decimal: {base_16}")
