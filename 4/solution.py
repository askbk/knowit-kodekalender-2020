def load_list():
    with open('leveringsliste.txt', 'r') as file:
        return [item.strip() for line in file.readlines() for item in line.split(",")]


def list_to_dict(lst):
    result = dict()

    for item in lst:
        name, count = item.split(": ")

        if not name in result:
            result[name] = 0

        result[name] += int(count)

    return result


def main():
    deliveries = load_list()
    deliveries_dict = list_to_dict(deliveries)

    ingredients_per_cake = {
            "sukker": 2,
            "mel": 3,
            "melk": 3,
            "egg": 1
            }

    cake_count = float("inf")

    for ingredient in deliveries_dict:
        cake_count = min(cake_count, deliveries_dict[ingredient]//ingredients_per_cake[ingredient])

    return cake_count

print(main())
