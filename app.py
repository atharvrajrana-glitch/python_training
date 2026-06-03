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
"""