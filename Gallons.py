
print("What is your name?")
name = input()
print('Hello,', name + "!" + ' What is the volume of your pool?')

volume = int(input())
gallonsCubic = volume*7.5
gallonsCylindrical = volume*5.875

print('You need', gallonsCubic, "gallons if your pool is a square or rectangle, or", gallonsCylindrical, 'gallons if your pool is cylindrical')

