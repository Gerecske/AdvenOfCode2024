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

for number in a:
    c = 0
    print(number)
    for other in b:
        if number == other:
            c = c +1


    output = output + c * number
    print("\n")
    print(c)
    print("\n")

print("\n")

print("Answer: " + str(output))