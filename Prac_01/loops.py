for i in range(1, 21, 2):
    print(i)
print("*******************************************")
for i in range(0, 100, 10):
    print(i)
print("*******************************************")
for i in range(20, 0, -1):
    print(i)

#"end=''" is not working, not sure how to bring the result in one line.

stars = int(input("please enter a number = "))
for i in range(1,stars+1):
    print("*")

 # for i in range (starting position, ending position, step)


print("******************************************************")

stars = int(input("please enter a number = "))
for i in range(1,stars+1):
    for j in range(1,i):
        print("*")
    print("\n")
