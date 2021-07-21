print("Insert digit: ")
num = int(input())
counter = 0
for element in range(1, num+1):
    counter += element ** 3
print(counter)