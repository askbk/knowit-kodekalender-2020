def tree_is_symmetrical(forest, pos):
    delta = 1
    while True:
        both_sides_blank = True
        left = pos - delta
        right = pos + delta

        for row in range(len(trees)):
            if forest[row][right] != forest[row][left]:
                return False

            if forest[row][left] != " " or forest[row][right] != " ":
                both_sides_blank = False

        if left == 0 or right == len(trees) - 1:
            return True

        if both_sides_blank:
            return True

        delta += 1

    return True


with open("forest.txt") as f:
    trees = list(reversed(f.readlines()))

count = 0

for column in range(len(trees[0])):
    if trees[0][column] != "#":
        continue

    if tree_is_symmetrical(trees, column):
        count += 1

print(count)
