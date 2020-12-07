with open("numbers.txt", "r") as file:
    numbers = list(map(lambda x: int(x), file.readline().split(",")))

print((100000 // 2) * (1 + 100000) - sum(numbers))
