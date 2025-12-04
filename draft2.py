a = [[1, 2, 3], [4, 5, 6, 3], [7, 8, 9]]

# b = list(filter((lambda x: not (x % 2)), a))

b = [a[j][i] for j in range(len(a[0])) for i in range(len(a))]
print(b)
