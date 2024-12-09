input = open('input.txt', 'r')

safe_data = 0

# Read the input
for line in input:
    data = line.split()
    if data[0] > data[1]:
        # dec
        for x in range(0, len(data)):
            if data[x] > data[x+1]:
                print(data[x]-data[x+1])
