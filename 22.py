f = open('names.txt')
contents = f.read()
namelist = contents.split(',')
names = [ x[1:-1] for x in namelist ]
names.sort()

sum = 0
place = 1
extra = ord('A') - 1


for name in names:
  minisum = 0
  for char in name:
    minisum += ord(char) - extra
  sum += minisum * place
  place += 1
print sum