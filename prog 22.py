username = input("your username")
password = input("enter password:")

password_dict ={}
password_dict[username]= password
print(password_dict)

#if password already exist
if username in password_dict:
    if password == password_dict[username]
        print("access granted")
    else:
        print("no no no access for u")
else:
    password_dict[username] = password
    print("you are addedto the userdb")
#cryptographic services- python.org this will encrypt the password


    #python program based website :- Hackerrank, lead code
    #project euler - simple one
