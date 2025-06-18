def even_sum(number):
    length=len(number)
    sum=0
    for i in range(length):
        if number[i]%2==0:
            sum=number[i]+sum
    
    return sum


if __name__== '__main__':
    number= list(map(int, input().split()))
    sum=even_sum(number)
    print(sum)