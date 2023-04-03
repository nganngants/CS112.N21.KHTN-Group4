from multiprocessing import Pool
import time
import random


# Merge 2 phần sau khi sort
def merge(data):
	left, right = data

	res = []

	n_left = len(left)
	n_right = len(right)
	i = j = 0

	# Chọn phần tử nhỏ nhất ở cả hai mảng để đưa vào vị trí tiếp theo
	while i < n_left and j < n_right:
		if left[i] <= right[j]:
			res.append(left[i])
			i += 1
		else:
			res.append(right[j])
			j += 1

	# Xếp lần lượt các phần tử còn lại vào phía sau các phần tử đã sắp xếp
	if i < n_left:
		res += left[i:]

	if j < n_right:
		res += right[j:]

	return res

# Hàm merge sort
def merge_sort(a):
	n = len(a)

	if n == 1:
		return a

	# Chia thành 2 phần
	mid = n // 2

	# Dùng merge sort cho phần bên trái
	left = merge_sort(a[:mid])
	# Dùng merge sort cho phần bên phải
	right = merge_sort(a[mid:])

	# Merge 2 phần đã sắp xếp
	res = merge((left, right))

	return res

# Chia đều n phần tử cho các bộ xử lý
def merge_sort_parallel(a, NUM_PROCESS):
	p = Pool(NUM_PROCESS)

	items = []

	for i in range(NUM_PROCESS):
		# processor thứ i sẽ xử lý trong khoảng (i * n // NUM_PROCESS, (i+1) * n // NUM_PROCESS - 1)
		low = i * n // NUM_PROCESS
		high = (i+1) * n // NUM_PROCESS - 1
		items.append(a[low:high+1])

	# Các phần sau khi xử lý sẽ đưa vào data
	data = p.map(merge_sort, items)

	# Phân processes để merge các phần lại
	
	while len(data) > 1:
		extra = data.pop() if len(data) % 2 == 1 else None
		data = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
		data = p.map(merge, data) + ([extra] if extra else [])

	return data[0]

def benchmark (func, a, NUM_PROCESS):
	start_time = time.perf_counter()
	a_parallel = func(a, NUM_PROCESS)
	end_time = time.perf_counter()
	print(f'Time taken: {end_time - start_time}s (parallel with {NUM_PROCESS} processes)')

if __name__ == '__main__':
	n = 0
	a = []

	n = 1000000

	for i in range(n):
		a.append(random.randint(0, 1000))

	# Tính thời gian xử lý khi sử dụng song song
	for NUM_PROCESS in range(2,5):
		benchmark(merge_sort_parallel, a, NUM_PROCESS)

	# Tính thời gian xử lý khi không sử dụng song song
	start_time = time.perf_counter()
	a_non_parallel = merge_sort(a)
	end_time = time.perf_counter()
	print(f'Time taken: {end_time - start_time}s (non-parallel)')

	# Xuất kết quả
	a_parallel = merge_sort_parallel(a, 4)
	f = open('output.txt', 'w')
	for x in a_parallel:
		f.write(str(x) + ' ')
	f.close()

	
	


