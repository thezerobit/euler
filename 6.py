max = 100

sumofsquares = 0;
for i in range(1, max + 1):
    sumofsquares += i * i;

squareofsums = 0;
for i in range(1, max +1):
    squareofsums += i

squareofsums = squareofsums * squareofsums

difference = abs(sumofsquares - squareofsums)

print difference
