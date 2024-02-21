with open('Dane_PR/dane.txt', 'r') as file:
    data = []
    for i in file:
        data.append(i.split())

file.close()

result = []

for i in range(1,200):
    for j in range(1,319):
        if abs(int(data[i][j]) - int(data[i][j + 1])) > 128:
            if [i, j] not in result:
                result.append([i, j])
            if [i, j + 1] not in result:
                result.append([i, j + 1])

for i in range(1,199):
    for j in range(1,320):
        if abs(int(data[i][j]) - int(data[i + 1][j])) > 128:
            if [i, j] not in result:
                result.append([i, j])
            if [i + 1, j] not in result:
                result.append([i + 1, j])

print(len(result))
