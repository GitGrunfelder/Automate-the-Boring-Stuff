grid = [['.', '.', '.', '.', '.', '.'], # x increases as you go right
        ['.', 'O', 'O', '.', '.', '.'], # y increases as you go down
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'], # need to read from top down first, and then move right.
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Hard coded solution
for y in range(6):
    for x in range(9):
        print(grid[x][y], end='')
    print()

print()

# Better Solution
for x in range(len(grid[0])): # for the length of the first inner list (6 loops)
    for y in range(len(grid)): # for count of items in outer list (9 times)
        print(grid[y][x], end='') 
    print()
        