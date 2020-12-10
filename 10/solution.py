def main(results):
    points = dict()
    winner = None
    for result in results:
        for i in range(len(result)):
            elf = result[i]

            if not elf in points:
                points[elf] = 0

            points[elf] += len(result) - i - 1

            if winner is None or points[elf] > points[winner]:
                winner = elf

    return winner, points[winner]


with open("leker.txt") as f:
    results = [line.strip().split(",") for line in f.readlines()]

print(main(results))