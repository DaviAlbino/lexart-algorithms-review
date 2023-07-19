def cyclotron(particle, matrix_size):
    matrix = [[1] * matrix_size for _ in range(matrix_size)]

    if particle == "e":
        for index in range(matrix_size):
            matrix[0][index] = particle
            matrix[index][matrix_size-1] = particle
        for _ in range(1, matrix_size-1):
            matrix[matrix_size-1][matrix_size - 1] = particle

    elif particle == "p":
        for index in range(matrix_size):
            matrix[0][index] = particle
            matrix[index][0] = particle
            matrix[index][matrix_size-1] = particle
            matrix[matrix_size-1][index] = particle
        matrix[matrix_size-1][matrix_size-1] = 1

    elif particle == "n":
        for index in range(matrix_size):
            matrix[0][index] = particle
            matrix[index][0] = particle
            matrix[index][matrix_size-1] = particle
            matrix[matrix_size-1][index] = particle

    return matrix


if __name__ == "__main__":
    matrix4 = cyclotron("p", 6)
    for row in matrix4:
        print(row)
