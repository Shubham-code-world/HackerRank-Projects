if __name__ == '__main__':
    names=[]
    both=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names=[name,score]
        both.append(names)
    both.sort(reverse=True)
    print(both)