import datetime
currentyear=datetime.datetime.now().year
birthyear=int(input("Enter the age: "))
age=currentyear-birthyear
print(f"your is {age}")