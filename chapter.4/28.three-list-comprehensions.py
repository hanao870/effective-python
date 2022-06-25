"""項目28:内包表記では、3 つ以上のしきを避ける."""


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat = [x for row in matrix for x in row]
    print(flat)
