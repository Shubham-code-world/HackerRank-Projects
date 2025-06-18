def reverse(string):
    for char in reversed(string):
        print(char, end='')
if __name__== '__main__':
    string=input()
    reverse(string)