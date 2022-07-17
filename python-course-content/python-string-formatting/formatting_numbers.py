""" 
Formatting Numbers
"""
x = 4687.4356789
print(f'{x:.6}') # Rounding (làm tròn) - 4687.44
print('{:.6}'.format(x)) # Rounding - 4687.44

print(f'{x:.3}') # 4.69e+03
print(f'{x:.3f}') # 4687.436

# 4687.435679 - Rounding
print(f'{x:f}') # default - 6 digits of precision

x = 1234567
print(f'{x:,}') # 1,234,567
print(f'{x:_}') # 1_234_567
print(f'{x:#}') # 1234567
print(f'{x: }') # | 1234567

x = 4687.4356789
print(f'{x:,.3f}') # 4,687.436
print(f'{x:_.3f}') # 4_687.436

print('-----------------------------------')

questions = 30
correct_answers = 23

division = correct_answers / questions
print(division) # 0.7666666666666667

# You got 76.67% correct! - Rounding
print(f'You got {division:.2%} correct!')
