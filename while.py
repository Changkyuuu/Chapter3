# while

count =1

while count < 5:
    print(count)
    # count = count + 1 밑에랑 같음
    count += 1

# 위 while 문과 동일한거를 for문으로
for count in range(1,5):
    print(count)

# 1~10까지 더하는 거 만들기

sum = 0
for i in range(1,11): # range 잡을때 []로 리스트로 잡아도 됨
    sum = sum + i
print(sum)

num = 0
sum = 0
while num <10: # 조건
    num += 1 # 1씩 증가
    sum = sum + num # 0+1+0+2~~~ 이렇게?
print(sum)

# 1~10 더하기 강사
s, i = 0, 1
while i <= 10:
    s += i
    i += 1
print(s)

# break, continue, else 사용하기

i = 0
while i < 10:
    i+= 1

    if i<5:
        continue
    print(i, end = '  ')

    if i > 10 : # 8일때는 아래 else 문 안탐
        break

else:
    print('else block')

# 무한루프


# i = 0
# while True :
#     print(i, end=' ')
#     if i > 5:
#         break
# else:
#     print('elso block')