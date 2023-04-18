import os
from random import randint
import random
import math

random.seed(199)

os.mkdir('giaitri')

def solve(a, b):
	return a ** b + b ** a

def create_test(id):
	test_path = os.path.join('giaitri', 'test' + str(id))
	os.mkdir(test_path)
	f_inp = open(os.path.join(test_path, 'giaitri.inp'), 'w')
	f_out = open(os.path.join(test_path, 'giaitri.out'), 'w')

	return f_inp, f_out

def subtask(low, high):
	for id in range(low, high+1):
		f_inp, f_out = create_test(id)

		q = randint(1, 2e2)
		f_inp.write(str(q) + '\n')
		for _ in range(q):
			a = randint(1, 1e3)
			b = randint(1, 1e3)
			f_inp.write(str(a) + ' ' + str(b) + '\n')

			res = solve(a, b)
			f_out.write(str(res) + '\n')

		f_inp.close()
		f_out.close()

def main():
	f_inp, f_out = create_test(1)

	q = 200
	f_inp.write(str(q) + '\n')
	for _ in range(q):
		a = 1
		b = 1
		f_inp.write(str(a) + ' ' + str(b) + '\n')

		res = solve(a, b)
		f_out.write(str(res) + '\n')

	f_inp.close()
	f_out.close()

	subtask(2, 19)

	f_inp, f_out = create_test(20)

	q = 200
	f_inp.write(str(q) + '\n')
	for _ in range(q):
		a = 1000
		b = 1000
		f_inp.write(str(a) + ' ' + str(b) + '\n')

		res = solve(a, b)
		f_out.write(str(res) + '\n')

	f_inp.close()
	f_out.close()

if __name__ == '__main__':
	main()