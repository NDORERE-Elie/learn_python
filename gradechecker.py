print("...........grade checker system..............")
name=input("Enter your name: ")
sub=int(input("enter number subject: "))
#total marks
max_marks=float(input("enter maximum marks: "))
total=sub*max_marks
obt=0
#get marks for each student

for i in range(sub):
    marks=float(input(f"enter marks for each subject {i+1} : "))
    obt=obt+marks
#calculate percentage
percentage=(obt*100)/total

#determine the grade
if(percentage>=80):
    grade="A"

elif(percentage>=70):
    grade="B"

elif(percentage>=60):
    grade="C"
   
elif(percentage>=50):
    grade="D" 

elif(percentage>=40):
    grade="F"
    
    #Display the result

print("...........RESULT............")
print(f"name : {name}")
print(f"total marks : {total}")
print(f"obtained marks : {obt}")
print(f"percentage : {percentage}")
print(f"Grade : {grade}")