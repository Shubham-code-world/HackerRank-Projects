if __name__ == '__main__':
    text=input()
    width=int(input())
for i in range(width+1):
    for j in range(i):
        print("-",end='')
    print(text,end='')


