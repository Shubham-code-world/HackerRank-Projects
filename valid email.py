import email.utils

lst=[]
n=int(input("Enter number of users: "))
for i in range(n):
    username = input("Enter the name: ")
    email_addr = input("Enter the address: ")
    full = f"{username} <{email_addr}>"
    lst.append(full)
    
    

for i in range(len(lst)):
    parsed = email.utils.parseaddr(lst[i])
    fort= email.utils.formataddr(parsed)
    if i in fort !="!":
        print(fort)
        
