# 1
Names = ['Александр','Алекс','Альберт']
Surnames = ['Вотяк','Вотяков','Вотякович']
Patronomic = ['Романович']
People = [f'{x} {y} {z}' for x in Names for y in Surnames for z in Patronomic]
for s in People:
    s = s.split(' ')
    print(f'Диплом с отличием вручается {s[0]}y {s[1]}y {s[2]}y.')

# 2
A = input()
B = int(input())
C = int(input())
print(f'{A}{B:04}-{C:03}')

# 3
A = int(input())
B = int(input())
print(f'{A:>7}')
print(f'{B:>7}')
print(f'{A+B:>7}')

# 4
S = 100000000
r = int(input())
k = int(input())
print(f'{S*((1 + r/100)**k):,.2f}')

# 5
for a in range(1,101):
    for b in range(a,101):
        if '0' in str(a*b):
            print(f'[DEBUG] {a=} {b=} result = {a*b}')

# 6
def ip_minecraft(a,b,c,d):
    if any(x < 0 or x >= 128 for x in [a, b, c, d]):
        return 'Значения не удовлетворяют ip'
    temp = [
        ('.'.join(['{:08b}'] * 4)),
        ('.'.join(['{:b}'] * 4)),
        ('.'.join(['{:o}'] * 4)),
        ('.'.join(['{}'] * 4)),
        ('.'.join(['{:x}'] * 4))
    ]
    answer = []
    for x in temp:
        answer.append(x.format(a,b,c,d))
    return answer

print(ip_minecraft(127,0,0,1))