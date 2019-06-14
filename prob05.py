# 선택정렬(제자리 정렬 알고리즘)을 적용하는 코드를 완성하세요.
# 문제에 주어진 배열 [ 5, 9, 3, 8, 60, 20, 1 ] 를 크기 순서대로 정렬하여 다음과 같은 출력이 되도록 완성하는 문제입니다.


def insertionsort(list):
    returnlist = list
    for i in range(len(returnlist)):
        for j in range(len(returnlist)-i-1):
            if returnlist[j] < returnlist[j+1]:
                temp = returnlist[j]
                returnlist[j] = returnlist[j+1]
                returnlist[j+1] = temp
    return returnlist


arr = [ 5, 9, 3, 8, 60, 20, 1 ]
print(insertionsort(arr))