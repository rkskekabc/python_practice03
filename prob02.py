# range() 함수와 유사한 frange() 함수를 작성해 보세요. frange() 함수는 실수 리스트를 반환합니다.


def frange(val, basic=0.0, step=0.1):
    returnlist = []
    if basic < val:
        startnum = basic
        endnum = val
    else:
        startnum = val
        endnum = basic
    while startnum < endnum:
        returnlist.append(round(startnum, 1))
        startnum += step

    return returnlist


print(frange(2))
print(frange(1.0, 2.0))
print(frange(1.0, 3.0, 0.5))