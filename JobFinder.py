def register():
    names=[]
    usernames=[]
    passwords=[]
    names.append(input("Enter your name:"))
    usernames.append(input("choose your username:"))
    passwords.append(input("choose your password:"))
    return usernames
def login(usernames,passwords):
    usernames=[]
    passwords=[]
    password=""
    username=""
    username=input("Enter your username:")
    password=input("Enter your Password:")
    if password==passwords[usernames.index(username)]:
       print("welcome")
    else:
       print("incorrect!")
