"""
# print 5*5 stars
i = 0
while i < 5:
    j = 0
    while j < 5:
        print('*', end = '')
        j += 1
    print()
    i += 1
"""

"""
# print triangle stars
i = 0
while i <= 5:
    j = 0
    while j < i:
        print('*', end = '')
        j += 1
    print()
    i += 1
"""
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f'{j} * {i} = {i*j}', end = '\t')
        j += 1
    print()
    i += 1