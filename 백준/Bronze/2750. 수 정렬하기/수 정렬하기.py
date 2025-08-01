N = int(input())
array = []

for _ in range(N):
    array.append(int(input()))

for _ in range(N-1):
    for i in range(N-1):
        if array[i] > array[i+1]:
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp
            
for j in range(N):
    print(array[j])