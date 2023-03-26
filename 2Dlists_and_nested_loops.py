number_grids = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grids[0][0])
print(number_grids[2][2])

for row in number_grids:
    for col in row:
        print(col)
        