password = str(input("Password"))
rpassword = str(input("Repeat password"))

while True:
    if password != rpassword:
        print("They do not match!")
        rpassword = str(input("Repeat password"))

    if password == rpassword:
        break

print("User account created!")