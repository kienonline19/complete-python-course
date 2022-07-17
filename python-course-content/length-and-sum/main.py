''' Length and Sum '''
grades = [80, 75, 90, 100]

total = sum(grades)
length = len(grades)

average = total / length
print(average)

grades = [80, 75, 90, 100] # best
grades = {80, 75, 90, 100} # worst
grades = (80, 75, 90, 100) # bad
