# for 반복문
a = ['cat', 'cow', 'tiger']
for animal in a:
    print(animal, end= ' ')
else:
    print('')

# 복합 자료형을 사용하는 for 문
for t in [('둘리',10),('마이콜',20),('도우넛',30)]:
    print('name:%s, age:%d'% t)


# for name,age in [('둘리',10),('마이콜',20),('도우넛',30)]:
#     print('name:[0], age:[1]'.format(name,age))
# 이거 나중에 확인

# 1~10 합구하기
s = 0
for i in range(1,11):
    s += i
print(s)

# break
for i in range(1,11):
    if i>5:
        break
    print(i, end=' ')
else:
    print(' ')

print('--------')

# continue
for i in range(10):
    print(i,end= ' ')
else:
    print('')
print('-------')


