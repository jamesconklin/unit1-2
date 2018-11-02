print('What year is it?')

year = int(input())

century = (year // 100 % 100) + 1

print("We are in the", century, "century")
