n = int(input("Фибоначчи:"))
fbn = []
a, b = 1, 1 
for x in range(n):
    fbn.append(a)
    a, b = b, a + b
print("Фибоначчи", fbn)


n 