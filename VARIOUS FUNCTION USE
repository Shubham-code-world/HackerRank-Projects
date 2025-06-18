if __name__ == '__main__':
    N = int(input())
    lst = []
    while N > 0:
        inputs = input().split()
        command = inputs[0]

        if command == "insert":
            i, e = map(int, inputs[1:3])
            lst.insert(i, e)
        elif command == "print":
            print(lst)
        elif command == "remove":
            rem = int(inputs[1])
            lst.remove(rem)
        elif command == "append":
            num = int(inputs[1])
            lst.append(num)
        elif command == "sort":
            lst.sort()
        elif command == "pop":
            lst.pop()
        elif command == "reverse":
            lst.reverse()
        N -= 1
