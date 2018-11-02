print('How far did the snail climb in feet?')
climb = int(input())

print('How far did the snail climb in fall? (make sure he fell a smaller distance than he climbed)')
fall = int(input())

days = (climb - fall)/climb

print('It will take the snail', days, 'days to climb back up.')
