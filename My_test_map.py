testmap = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 2, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 3, 2, 3, 1, 2, 1, 2, 2, 2, 1, 1, 1, 2, 3, 3, 3, 2, 2, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 2, 2, 3, 3, 2, 2, 3, 2, 3, 4, 2, 2, 2, 2, 2, 3, 3, 5, 4, 2, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 2, 2, 2, 2, 1, 1, 2, 3, 3, 4, 4, 3, 3, 4, 3, 3, 3, 5, 4, 3, 2, 1, 1, 0, 0, 0],
    [0, 0, 1, 2, 2, 3, 1, 1, 0, 0, 2, 2, 2, 3, 4, 4, 4, 4, 3, 2, 3, 3, 3, 4, 3, 2, 1, 0, 0, 0],
    [0, 0, 1, 2, 3, 3, 1, 0, 0, 0, 1, 2, 1, 2, 3, 4, 4, 3, 2, 1, 2, 2, 3, 3, 4, 2, 1, 1, 0, 0],
    [0, 1, 1, 2, 3, 2, 0, 0, 0, 0, 0, 1, 1, 2, 3, 4, 4, 3, 2, 1, 1, 1, 2, 3, 3, 3, 2, 1, 1, 0],
    [0, 1, 2, 3, 3, 2, 0, 0, 0, 0, 0, 1, 2, 3, 3, 3, 3, 2, 1, 0, 0, 0, 1, 2, 3, 3, 2, 1, 1, 0],
    [0, 1, 2, 2, 2, 1, 0, 0, 0, 0, 1, 1, 2, 3, 3, 3, 2, 1, 0, 0, 0, 0, 1, 2, 3, 3, 2, 1, 1, 0],
    [0, 1, 2, 3, 2, 1, 0, 0, 0, 0, 1, 2, 2, 3, 3, 2, 1, 0, 0, 0, 0, 0, 1, 2, 3, 3, 2, 2, 1, 0],
    [0, 1, 2, 3, 2, 1, 0, 0, 0, 1, 2, 3, 4, 4, 4, 3, 2, 1, 0, 0, 0, 1, 2, 3, 4, 3, 2, 1, 1, 0],
    [0, 1, 2, 3, 2, 1, 0, 0, 0, 1, 2, 3, 4, 4, 4, 3, 2, 1, 1, 0, 1, 2, 4, 4, 5, 3, 2, 1, 0, 0],
    [0, 1, 2, 3, 2, 1, 0, 0, 0, 1, 2, 2, 3, 4, 4, 3, 2, 2, 2, 1, 1, 2, 4, 4, 3, 2, 1, 1, 0, 0],
    [0, 1, 2, 3, 3, 2, 0, 0, 0, 0, 1, 2, 4, 5, 5, 4, 4, 2, 3, 2, 2, 3, 5, 5, 3, 2, 1, 0, 0, 0],
    [0, 1, 2, 3, 3, 3, 2, 0, 0, 1, 1, 2, 3, 4, 5, 5, 4, 3, 3, 3, 3, 4, 5, 4, 3, 2, 1, 0, 0, 0],
    [0, 1, 2, 2, 3, 4, 3, 2, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5, 4, 4, 5, 5, 4, 3, 2, 1, 1, 0, 0, 0],
    [0, 1, 1, 2, 3, 4, 4, 4, 4, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 3, 2, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 2, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 3, 2, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 2, 3, 4, 4, 4, 4, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


B = [[1, 2, 9], [2, 8, 4], [3, 5, 5]]
