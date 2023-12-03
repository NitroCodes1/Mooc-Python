my_list = []
print(f"The list is now {my_list}")

maths = str(input("a(d)d, (r)emove or e(x)it:"))

while maths != 'x':
    if maths == "d":
        if my_list == []:
            my_list.append(1)
            print(f"The list is now {my_list}")
        else:
            my_list.append(my_list[-1] + 1)
            print(f"The list is now {my_list}")
        maths = str(input("a(d)d, (r)emove or e(x)it:"))
    elif maths == "r":
        my_list.pop(-1)
        print(f"The list is now {my_list}")
        maths = str(input("a(d)d, (r)emove or e(x)it:"))
    else:
       break
print("Bye!")