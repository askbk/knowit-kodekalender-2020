def load_list():
    with open("godteri.txt", "r") as f:
        return [int(i) for i in f.readline().split(",")]


def main(elf_count, candy_list):
    candy_per_elf = 0
    total_candy = 0

    for candy_count in candy_list:
        total_candy += candy_count
        if total_candy % elf_count == 0:
            candy_per_elf = total_candy // elf_count

    return candy_per_elf


print(main(9, [10, 14, 14, 13, 13, 13, 15, 14, 11, 15, 11]))
print(main(127, load_list()))
