import os
from random import randint
import random
import math

random.seed(199)

os.mkdir('modulo')

def solve(ty, a, b, c):
	if ty == 1:
		return ((a % c) * (b % c)) % c
	else:
		b, c = min(b, c), max(b, c)

		d = a // math.lcm(b, c)
		if a % b == a % c:
			return d * b + a % b
		return d * b + b - 1

def create_test(id):
	test_path = os.path.join('modulo', 'test' + str(id))
	os.mkdir(test_path)
	f_inp = open(os.path.join(test_path, 'modulo.inp'), 'w')
	f_out = open(os.path.join(test_path, 'modulo.out'), 'w')

	return f_inp, f_out

def subtask1(low, high):
	for id in range(low, high+1):
		f_inp, f_out = create_test(id)

		q = randint(1, 1e5)
		f_inp.write(str(q) + '\n')
		for _ in range(q):
			ty = 1
			a = randint(1, 1e9)
			b = randint(1, 1e9)
			c = randint(1, 1e9)
			f_inp.write(str(ty) + ' ' + str(a) + ' ' + str(b) + ' ' + str(c) + '\n')

			res = solve(ty, a, b, c)
			f_out.write(str(res) + '\n')

		f_inp.close()
		f_out.close()

def subtask2(low, high):
	for id in range(low, high+1):
		f_inp, f_out = create_test(id)

		q = randint(1, 1e3)
		f_inp.write(str(q) + '\n')
		for _ in range(q):
			ty = 2
			a = randint(1, 1e4)
			b = randint(1, min(a, 1e2))
			c = randint(1, min(a, 1e2))
			f_inp.write(str(ty) + ' ' + str(a) + ' ' + str(b) + ' ' + str(c) + '\n')

			res = solve(ty, a, b, c)
			f_out.write(str(res) + '\n')

		f_inp.close()
		f_out.close()

def subtask3(low, high):
	for id in range(low, high+1):
		f_inp, f_out = create_test(id)

		q = randint(1, 1e5)
		f_inp.write(str(q) + '\n')
		for _ in range(q):
			ty = randint(1, 2)
			a = randint(1, 1e9)
			b = randint(1, min(a, 1e5))
			c = randint(1, min(a, 1e5))
			f_inp.write(str(ty) + ' ' + str(a) + ' ' + str(b) + ' ' + str(c) + '\n')

			res = solve(ty, a, b, c)
			f_out.write(str(res) + '\n')

		f_inp.close()
		f_out.close()

def subtask4(low, high):
	for id in range(low, high+1):
		f_inp, f_out = create_test(id)

		q = randint(1, 1e5)
		f_inp.write(str(q) + '\n')
		for _ in range(q):
			ty = randint(1, 2)
			a = randint(1, 1e18)
			b = randint(1, min(a, 1e12))
			c = randint(1, min(a, 1e12))
			f_inp.write(str(ty) + ' ' + str(a) + ' ' + str(b) + ' ' + str(c) + '\n')

			res = solve(ty, a, b, c)
			f_out.write(str(res) + '\n')

		f_inp.close()
		f_out.close()

def main():
	subtask1(1, 8)
	subtask2(9, 16)
	subtask3(17, 24)
	subtask4(25, 40)

if __name__ == '__main__':
	main()