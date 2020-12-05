def area(coordinates):
    area = 0
    for i in range(len(coordinates)):
        area += (coordinates[i-1][0] + coordinates[i][0]) * (coordinates[i-1][1] - coordinates[i][1])

    return -area / 2


def parse_route(route):
    directions = list(route)

    x, y = 0, 0
    coordinates = [(0, 0)]
    previous = directions[0]

    for direction in directions:
        if not direction == previous:
            coordinates.append((x, y))

        previous = direction

        if direction == "H":
            x += 1

        if direction == "O":
            y += 1

        if direction == "V":
            x -= 1

        if direction == "N":
            y -= 1

    return coordinates


def main(route):
    coordinates = parse_route(route)

    return area(coordinates)


print(main("HHOOVVNN"))
print(main("HHHHHHOOOOVVNNNVVOVVNN"))

with open("rute.txt", "r") as f:
    print(main(f.readline().strip()))
