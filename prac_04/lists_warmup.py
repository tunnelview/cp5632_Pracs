
#          0  1  2  3  4  5  6
numbers = [3, 1, 4, 1, 5, 9, 2]
#         -7 -6 -5 -4 -3 -2 -1

#numbers[0] - 3
#numbers[-1] - 2
#numbers[3] - 1
#numbers[:-1] - [3,1,4,1,5,9]
#numbers[3:4] - [1]
#5 in numbers - True #(Membership Test)
#7 in numbers - False
#"3" in numbers  - False #(As literal String)
#numbers + [6, 5, 3] - [3,1,4,1,5,9,2,6,5,3]


#          0  1  2  3  4  5  6
numbers = [3, 1, 4, 1, 5, 9, 2]
#         -7 -6 -5 -4 -3 -2 -1
numbers[0] = "ten"
print(numbers)
numbers[6] = 1
print(numbers)
print(numbers[2:])
print(9 in numbers)



