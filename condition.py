# if -elso
a = 1
if a > 5:
    print('big')

a = 1
if a < 5:
    print('big') # 요고만 출략

a = 3
if a > 5:
    print('big')
else:
    print('small')

# a가 5보다 크면 big를 출력하고 아니면 small을 출력해라

# if - elif -
n = -1
if n > 0:
    print('양수')
elif n < 0:
    print('음수')
else:
    print('0')

# spam : 100
# egg : 500
# spagetti : 2000

price = 0
goods = 'egg'
if goods == 'spam':
    price = 100
elif goods == 'egg':
    price = 500
elif goods == 'spagetti':
    price == 2000

print(price)

# 상황연산자
# message = a>5 ? 'big' : 'small' 다른언어에서는

a = 5
print( 'big 'if a > 5 else 'small')