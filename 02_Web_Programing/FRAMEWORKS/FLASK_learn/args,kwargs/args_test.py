# *args 는 길이의 제한이 없는 파라미터이다.
# 함수 내부에서는 길이가 몇개가 들어오든 배열로 처리가 된다

def myFunction(*args):
    print(args)
    result = 1
    for arg in args:
        result *= arg
    return result
#. 가변 길이가 가능한지 실험해보자
print("곱하기 결과는 ", myFunction(2,4,6,8,10))
print("곱하기 결과는 ", myFunction(3,5,7))