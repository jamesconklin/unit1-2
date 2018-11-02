print('Give me any 2 digit number')

number = int(input())

onesA = number // 10
onesB = onesA * 10
onesPlace= number - onesB

tensPlace = number // 10 % 10

print(onesPlace,tensPlace)
