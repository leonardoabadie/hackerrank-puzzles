def isCavity(g, c, i, j):
	if ((g[i][j-1] < c > g[i][j+1]) and (g[i-1][j] < c > g[i+1][j])):
    return True

	return False

def cavityMap(grid):
	length = len(grid)
	if (length == 2):
		return grid

	for i in range(1, length - 1):
		for j in range(1, length - 1):
			cell = grid[i][j]
			if (isCavity(grid, cell, i, j)):
				tmp = list(grid[i])
				tmp[j] = "X"
				grid[i] = "".join(tmp)

	return grid
