# 구구단 중에 특정 곱셈을 만들고 그 답을 선택하는 프로그램을 작성하는 문제입니다.
# 답을 포함하여 9개의 정수가 아래와 같은 형태로 출력되고 사용자는 답을 골라 입력하게 됩니다.
# 프로그램은 정답 여부를 다시 출력합니다.
import random


def shuffle(values):
    for n in range(0, len(values)):
        num = random.randrange(len(values))
        temp = values[n]
        values[n] = values[num]
        values[num] = temp


items = set()
for i in range(2, 10):
    for j in range(2, 10):
        items.add(i * j)

items = list(items)
shuffle(items)

firstnum = random.randrange(9) + 1
secondnum = random.randrange(9) + 1
answer = firstnum * secondnum

answerlist = items[0:9]

if answer not in answerlist:
    answerlist[random.randrange(9)] = answer
print(answerlist)

inputnum = 0

while True:
    print(firstnum, 'x', secondnum, '= ?')
    print()

    print('{0}\t{1}\t{2}\n{3}\t{4}\t{5}\n{6}\t{7}\t{8}'.format(*answerlist))

    print()
    inputnum = int(input('answer: '))
    if inputnum == answer:
        print('정답')
        break
    else:
        print('오답')
