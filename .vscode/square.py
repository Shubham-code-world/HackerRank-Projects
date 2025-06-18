def square(num):
    a=map(lambda x: x*x, num)
    print(list(a))

if __name__== '__main__':
    num=list(map(int,input().split()))
    square(num)