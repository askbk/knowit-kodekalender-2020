import numpy as np


def get_matrix():
    with open("matrix.txt", "r") as f:
        return np.array([np.array(list(line.strip())) for line in f.readlines()])


def get_wordlist():
    with open("wordlist.txt", "r") as f:
        return [line.strip() for line in f.readlines()]


def get_matrix_as_strings(matrix):
    lr_diagonals = [
        "".join(np.diagonal(matrix, offset=k))
        for k in range(-len(matrix[:, 0]) + 1, len(matrix[0, :]))
    ]
    rl_diagonals = [
        "".join(np.fliplr(matrix).diagonal(offset=k))
        for k in range(-len(matrix) + 1, len(matrix))
    ]
    columns = ["".join(matrix[:, i]) for i in range(len(matrix[:, 0]))]
    rows = ["".join(matrix[i, :]) for i in range(len(matrix[0, :]))]

    return lr_diagonals + rl_diagonals + columns + rows


def is_word_in_matrix_strings(word, matrix_strings):
    for string in matrix_strings:
        if word in string:
            return True

        if word[::-1] in string:
            return True

    return False


def main():
    matrix = get_matrix()
    words = get_wordlist()
    matrix_strings = get_matrix_as_strings(matrix)

    for word in words:
        if not is_word_in_matrix_strings(word, matrix_strings):
            print(word)


main()
