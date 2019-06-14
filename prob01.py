# 다음 세 개의 리스트가 있을 때,
# subs = ['I', 'You']
# verbs = ['Play', 'Love']
# objs = ['Hockey', 'Football']
# 
# 3형식 문장을 모두 출력해 보세요. 반드시 comprehension을 사용합니다.

subs = ['I', 'You']
verbs = ['Play', 'Love']
objs = ['Hockey', 'Football']

for sub in subs:
    for verb in verbs:
        for obj in objs:
            print('{0} {1} {2}'.format(sub, verb, obj))
