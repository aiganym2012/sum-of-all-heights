# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
a=0
for heights in student_heights:
  a+=heights

b=0
for sum in student_heights:
  b+=1
#totoal height

avarage_height= round(a/b)
print(avarage_height)
