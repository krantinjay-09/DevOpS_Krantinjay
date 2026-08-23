print("Enter your mark")
mark=int(input())
if mark >= 90:
   grade="A"
elif mark >= 80:
   grade="B"
elif mark >= 70:
   grade="C"
elif mark >= 60:
   grade="D"
else:
   grade="F"
print("Your grade is", grade)     