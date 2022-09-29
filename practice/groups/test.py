def show(left, right):
    if left > right:
        print("Left Bias!")
    elif right > left:
        print("Right Bias!")
    else:
        print("Symmertical String!")


s = input()
length = len(s)
half = length // 2

"""
    0123456
s = abcdefg
s = amaama
"""
if length % 2 == 0:
    print("There is no central point.")
    show(s[:half], s[half:])
else:
    print(f"The central point of the string is {s[half]}.")
    show(s[:half], s[half+1:])
