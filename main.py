i = [1,2,3,4]
w = [0.2,0.8,-0.5, 0.1]

b = 2

output = 0

for index in range(len(i)):

    output += i[index] * w[index]

total = output + b


print(total)
