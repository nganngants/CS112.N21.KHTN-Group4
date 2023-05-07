cols = None
cells = None
res = []
n = None

def init():
	global cols, cells

	cols = [False for _ in range(n)]
	cells = [[False for j in range(n)] for i in range(n)]

def check_diagonal(row, col, i, j):
	row1 = row
	col1 = col
	while row1 + i >= 0 and col1 + j >= 0 and row1 + i < n and col1 + j < n:
		if cells[row1 + i][col1 + j]:
			return False

		row1 += i
		col1 += j

	return True

def check(row, col):
	if cols[col]:
		return False

	if not check_diagonal(row, col, -1, -1) or not check_diagonal(row, col, 1, -1) or not check_diagonal(row, col, -1, 1) or not check_diagonal(row, col, 1, 1):
		return False

	return True


def process(row):
	global res

	if row == n:
		res_cell = []
		for i in range(n):
			res_row = ''
			for j in range(n):
				if cells[i][j]:
					res_row += 'Q'
				else:
					res_row += '.'
			res_cell.append(res_row)
		res.append(res_cell)

	for col in range(n):
		if not check(row, col):
			continue

		cols[col] = True
		cells[row][col] = True

		process(row + 1)

		cols[col] = False
		cells[row][col] = False


if __name__ == '__main__':
	n = int(input())

	init()

	process(0)
	print(res)


