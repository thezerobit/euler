f = open('words.txt')
contents = f.read()
wordrough = contents.split(',')
words = [ x[1:-1] for x in wordrough ]

triangles = {}
for x in xrange(1,1000):
  tri = (x * (x - 1)) / 2
  triangles[tri] = tri

def sumofdigits(word):
  total = 0
  for letter in word:
    total += ord(letter) - ord('A') + 1
  return total

count = 0

for word in words:
  if sumofdigits(word) in triangles:
    count += 1

print count