def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b

# print(__name__)  #특수내장변수
if __name__ == "__main__":
    n1, n2 = [int(e) for e in input("2개의 정수 입력: ").split()]
    print(add(n1,n2))