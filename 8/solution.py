def distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def new_santa_position(pos, target_pos):
    if pos[0] > target_pos[0]:
        return (pos[0] - 1, pos[1])
    if pos[0] < target_pos[0]:
        return (pos[0] + 1, pos[1])
    if pos[1] > target_pos[1]:
        return (pos[0], pos[1] - 1)
    if pos[1] < target_pos[1]:
        return (pos[0], pos[1] + 1)

    raise ArithmeticError


def calculate_world_time(time, locations, santa_position):
    new_time = dict(time)

    for name, position in locations.items():
        santa_distance = distance(position, santa_position)
        if santa_distance == 0:
            continue
        if santa_distance < 5:
            new_time[name] += 0.25
        elif santa_distance < 20:
            new_time[name] += 0.5
        elif santa_distance < 50:
            new_time[name] += 0.75
        elif santa_distance >= 50:
            new_time[name] += 1

    return new_time


def main(locations, route):
    santa_position = (0, 0)
    time = {location: 0 for location in locations}

    for location in route:
        while distance(santa_position, locations[location]) > 0:
            santa_position = new_santa_position(santa_position, locations[location])
            time = calculate_world_time(time, locations, santa_position)

    min_time, max_time = float("inf"), 0

    for location, local_time in time.items():
        min_time = min(min_time, local_time)
        max_time = max(max_time, local_time)

    return max_time - min_time


def parse_location(location_line):
    name, position_string = location_line.split(":")
    (x, y) = position_string.strip()[1:-1].split(",")
    position = (int(x), int(y))

    return name, position


with open("test.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    locations = dict()

    for line in lines[:2]:
        name, position = parse_location(line)
        locations[name] = position

    route = lines[2:]

print(main(locations, route))

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    locations = dict()

    for line in lines[:50]:
        name, position = parse_location(line)
        locations[name] = position

    route = lines[50:]

print(main(locations, route))