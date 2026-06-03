#question 1
"""
a = 5
b = 10 
a = a+b
b = a-b
a = a-b
print(a,b)

Question 2
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"name: {name} , age: {age}")

Question 3
number = int(input("Enter a number: "))

if number % 2 == 0 :
    print("EVEN")
else:
    print("ODD")

Question 4
c = int(input("Enter Celsius: "))
f = (c * 9/5) +32
print (f)

f = int(input("Enter Fahrenheit: "))
c = (f - 32) * 5/9
print(c)

first_name , last_name = input("Enter your name :").split()
print(f"your name is {first_name} {last_name}")

template = "Hello {user} your Rank is {rank}"
print(template.format(user="Bob", rank=12))

name = "pen"
price= 10
print("Item: %s costs $%d" % (name, price)) 


year = int(input("Enter year: "))

if year % 4 == 0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")

s = "ruur"
res = s == s[::-1]
print(res)

des = {
    "key1":"value1",
    "key2":"value2",
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
}
#print(des["key1"])
des["key3"] = "value3"
des.update({"key4":"value4"})
des['skills'].append("HTML")

#print(des.get("key5"))
del des['key4']
key_value = des.keys()
#print(key_value)
values = des.values()
#print(values)
#print(len(des))
#t_list = list(des.items())
#keys = list(des.values())
#print(keys)

text = "atharvraj"
des2 = {}

for char in text:
    if char in des2:
        des2[char] += 1
    else:
        des2[char] = 1
print(des2)


num1 = int(input("Enter number1: "))
sign = input("Enter sign: ")
num2 = int(input("Enter number2: "))

if sign == "+":
    res = num1 + num2
elif sign == "-":
    res = num1 - num2
elif sign == "/":
    res = num1 / num2
elif sign == "*":
    res = num1 * num2
print(res)

fruits = ['banana', 'orange', 'mango', 'lemon']
set1 = set(fruits)
print(set1)
fruits.sort()
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort(reverse= False)
print(fruits)

tul = ('banana', 'orange', 'mango', 'lemon') 
tul2 =('banana','lemon')
new_tul = tul + tul2 
print(new_tul)

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item6', 'item7', 'item8'}
set3 = st1.union(st2)
print(set3)

ternary operator:
age = 20 
stauts = "Adult" if age >=18 else "Minor"
print(stauts)


i = 0

for i in range(101):
    if i % 2 == 0:
        print(i)
    i+=1
""" 

# a = 2 ** 3 
# print(a)

# a = 22 / 8 
# print(a)

# a = 'Atharv' * 3 
# print(a)
# while True:
#     print("Who are you?")
#     name = input('>')
#     if name != 'Joe':
#         continue
#     print("Hello , Joe.")
#     password = input('>')
#     if password == 'swordfish':
#         break
#   print('Access granted.')

# for i in range(5):
#     print('on this iteration, i is set to '+ str(i))
# print('Goodbye')
   
# total = 0 
# for num in range(101):
#     total = total + num
# print(total)

# for i in range(0 , 10):
#     print(i)

# def say_hello(name):
#     print('Good morning,' + name)

# say_hello('Atharv')

# def spam():
#    eggs = 'sss'
# spam()
# print(eggs)

# for x in range(3):
#     print(x)
# else:
#     print("Loop finished cleanly!")

# for x in range(2):
#     for y in range(3):
#         print(x,y)

# l = ['veer','atharv','rana']
# # print(l[0])
# l.append("raj")
# a = ['shiv','yash','singh']
# l.extend(a)
# l.insert(2,'loops')
# l.remove('loops')
# r = l.pop(1)
# l.sort(reverse = True)
# # l.clear()
# # print(r)

# # print(l[:3])
# squares = [x**2 for x in range(5) if x % 2 == 0 ]
# print(squares)

# matrix = [ 
#     [1,2,3],
#     [4,5,6]
# ]
# print(matrix[0][1])

t = ('veer','rana','singh')
t2 = (2,3,4)
# print(t+t2)
# print((1 , 2 )*3)
# print("rana" not in t)
# lat , lon , laa = t 
# print(lat)
# print(t)

dic = {
    "key1":"value1",
    "key2":"value2",
    "key3":"value3"
}
dic['key1'] = ['value1.0']
# print(dic['key1'])
dic["key4"] = ['value4','value4.0.1']
# del dic['key1']
# print(dic.get("key2"))
# print(dic)
# all_keys = dic.keys()
# print(all_keys)

# all_values = dic.values()
# print(all_values)

# for key, val in dic.items():
#     print(f"{key}: {val}")

# get_val = dic.pop("key1")
# print(get_val)
# dic.clear()
# print(dic)
# for i , j in dic.items():
#     print(i , j)

# for name in dic.values():
#     print(name)

# for name in dic:
#     score = dic[name]
#     print(f"{name}: {score}")

# for i in dic.values():
#     print(i)

my_family = {
    "child1": {"name":"veer","age:25"}
    "child2":{"name":"atharv","age:23"}
    "child3":{"name: raj"}
}