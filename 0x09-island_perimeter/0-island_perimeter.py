#!/usr/bin/python3
"""Island Perimeter - ALX Interview"""

def check_val(perimeter):
        """
        checking for a value
        """
        if perimeter == 0:
            return 1
        return 0

def island_perimeter(grid):
    """Island Perimeter
    """
    
    row = len(grid)
    col = len(grid[0])
    assert 1 <= row <= 100 and 1 <= col <= 100, "length must be between 1 an 100"

    # initialize the perimeter counter
    perimeter = 0
    # iterate over each cell in the grid
    for i in range(row):
        for j in range(col):
            assert (grid[i][j] == 0) or (grid[i][j] == 1),\
                                        "grid numbers must be 0 or 1"
            # check if the cell is land
            if grid[i][j] == 1:
                if i - 1 < 0:
                    perimeter += 1
                else:
                    perimeter += check_val(grid[i - 1][j])
                if j - 1 < 0:
                    perimeter += 1
                else:
                    perimeter += check_val(grid[i][j - 1])

                try:
                    perimeter += check_val(grid[i + 1][j])
                except IndexError:
                    perimeter += 1
                try:
                    perimeter += check_val(grid[i][j + 1])
                except IndexError:
                    perimeter += 1

    return perimeter
