x = 6
value = x if x < 10 else "Invalid value" # 6
print(value)

x = 10
value = x if x < 10 else "Invalid value" # Invalid value

print(value)

x = 16
val = x if x < 10 else "Invalid value" if x < 15 else "Super invalid value"
print(val) # Super invalid value

x = 10

if x < 10:
    val = x
else:
    val = "Invalid value"

# Invalid value
print(val)
