"""
File: largest_digit.py
Name: Jess
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: integers
	:return: the largest digit
	"""
	n = abs(n)  # absolute the value

	if n < 10:
		return n
	else:
		return find_helper(n, 0)


def find_helper(abs_n, largest_digit):
	# base case
	if abs_n == 0:
		return largest_digit

	else:
		# get value of the digit
		record = abs_n % 10
		# choose
		if record > largest_digit:
			largest_digit = record
		# explore
		return find_helper(abs_n//10, largest_digit)


if __name__ == '__main__':
	main()
