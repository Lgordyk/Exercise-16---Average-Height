# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

total = 0

for height in student_heights:
    total = total + height

total_heights = total/(n+1)

print(int(round(total_heights)))
#Write your code below this row 👇




