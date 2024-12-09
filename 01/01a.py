input = open('input.txt', 'r')

a = []
b = []

# Read the input
for line in input:
    a.append(int(line.split()[0]))
    b.append(int(line.split()[1]))

a.sort()
b.sort()

output = 0

for x in range(0, len(a)):
    dif = abs(b[x]-a[x])
    output = output + dif

print(output)