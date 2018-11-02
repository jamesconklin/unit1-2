print('What is the first students name?')
nameFirst = input()

print('Hello ' + nameFirst + ', what is your GPA?' )

gpaFirst = float(input())

print('What is the second students name?')
nameSecond = input()

print('Hello ' + nameSecond + ', what is your GPA?' )

gpaSecond = float(input())

print('What is the third students name?')
nameThird = input()

print('Hello ' + nameThird + ', what is your GPA?' )

gpaThird = float(input())

print('What is the fourth students name?')
nameFourth = input()

print('Hello ' + nameFourth + ', what is your GPA?' )

gpaFourth = float(input())

gpaTotal = gpaFirst + gpaSecond + gpaThird + gpaFourth
average = gpaTotal/4

print("The average of your four GPAs is:", float(average))


