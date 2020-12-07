def find_prime(n):
    if n == 2:
        return 2

    for i in range(n, 2, -1):
        is_prime = True

        for j in range(2, i // 2):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            return i


def number_contains_seven(n):
    c = int(n)
    while c > 1:
        a = c % 10
        c = c // 10

        if a == 7:
            return True

    return False


def count_delivered_gifts(population):
    count = 0
    to_skip = 0

    for i in range(population + 1):
        if to_skip > 0:
            to_skip -= 1
            continue

        if number_contains_seven(i):
            to_skip = find_prime(i)
            continue

        count += 1

    return count


print(count_delivered_gifts(5433000))
