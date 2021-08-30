#1. write name in file
#name = input("please enter your name: ")
#file=open("name.txt",'w')
#file.write(name)
#file.close()

#2. Read name from file
#file=open("name.txt",'r')
#name = file.readline()
#print(name)
#file.close()

#List = ["17 \n","42 \n","400\n"]
#file = open("numbers.txt",'w')
#file.writelines(List)
#file.close()
file=open("numbers.txt",'r')
num_1=int(file.readline())
num_2=int(file.readline())
print(num_1+num_2)
file.close()



