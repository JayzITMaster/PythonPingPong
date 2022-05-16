name = "Jahmur" # comment assigning of variable
age = 24

country = "BELIZE"
place = "Belmopan"
#print("my name is : {} and age is : {}".format(name,age))

#print("my name is :%s and age is : %s"%(name,age))

#print ("my name is : {}, age is :{}, i stays at {}: country {}".format(name,age,country,place))

# def say_hi(name,age):
#     print("Hello " + name + ", you are " + age)
    
# say_hi("Mike", "35")
# say_hi("Steve", "70")

# def cube (num):
#    return num*num*num
    
# result = cube(4)   
# print(result)

is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male nor tall")