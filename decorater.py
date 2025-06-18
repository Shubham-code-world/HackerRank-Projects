def greet(fx):
    def mfx(*args, **kwargs):
        print("Good morning ")
        fx(*args, **kwargs)
        print("Thanks for using")
    return mfx
@greet
def hello():
    print("Hello world")
hello()

@greet
def add(a,b):
    print(a+b)

a=int(input("enter the Number : "))
b=int(input("Enter the second number : "))
obj=add(a,b)