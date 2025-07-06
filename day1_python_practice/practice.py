"""
#input from user,mad lib game
name=input("enter name:")
age=input("enter age:")
color=input("enter color:")
print("hello iam "+name)
print("iam "+age+" years old")
print("i like "+color+" colour")
"""

"""
#basic calculator
x=input("enter first number:")
y=input("enter second number:")
result=x+y
#for integer
print(result)
result=int(x)+int(y)
#for floating points
print(result)
result=float(x)+float(y)
"""

"""
creation of list and list operations(mutable)
age=[26,28,30,27,17]
friends=["john","jack","jane","smith","nick","john"]
friends.sort()
print(friends)
age.sort()
print(age)
age.reverse()
print(age)
friends.extend(age)
friends.append("jim")
friends.insert(1,"kevin")
friends.remove("jim")
print(friends.index("jack"))
print(friends.count("john"))
friends.pop()
print(friends)
print(friends[1])
print(friends[-2])
print(friends[1:4])
friends[1]="mike"
print(friends[1])
friends2=friends.copy()
print(friends2)
friends.clear()
print(friends)
"""

"""
#creation of tuple and tuple operations(immutable)
coordinates=(2,3,7,8,9,4,9)
print(coordinates)
print(coordinates[4])
coordinate=[(1,2),(2,3),(3,4),(4,5)]
print(coordinate)
"""

""""
#functions
#method1
def example(name,age):
    print("hello "+name+" you're "+age)
example("john","25")
example("jack","22")
example("jane","23")
#method2
def example(name,age):
    print("hello "+name+" you're "+str(age))
example("john",25)
example("jack",22)
example("jane",23)
"""

#return statements