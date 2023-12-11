print("Welcome To BMI Calculator")
height = float(input("Your Height\n"))
weight = int(input("Your Weight in KG\n"))

bmi = weight // height ** 2
print(int(bmi))