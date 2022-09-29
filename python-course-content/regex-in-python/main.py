import re

"""
email = 'jose@tecladocode.com'
expression = '[a-z]+'

matches = re.findall(expression, email)

print(matches)
name, *rest = matches
print(name)

domain = '.'.join(rest)
print(domain)

print('-' * 40)

expression = '[a-z\.]+'
matches = re.findall(expression, email)
print(matches)

name, domain = matches

print(name)
print(domain)

print('-' * 40)

parts = email.split('@')
print(parts)

name, domain = parts
print(name)
print(domain)
"""

#Exmaple 2
price = 'Price: $18,649.50'
expr = 'Price: \$([0-9,]*\.\d*)' # 472635872372358.584674876

matches = re.search(expr, price)
print(matches.group(0)) # entire match
print(matches.group(1)) # first thing in brackets

price_without_comma = matches.group(1).replace(',', '')
price_number = float(price_without_comma)
print(price_number)
