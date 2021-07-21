n = int(input())
m = int(input())
counter = 0
for element in range(n, m+1):
    counter += element ** 3
print(counter)
