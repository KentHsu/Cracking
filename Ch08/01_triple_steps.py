
def memorize(func):
	table = {}
	def memorizer(n):
		if n not in table:
			table[n] = func(n)
		return table[n]
	return memorizer


@memorize
def fn(n):
	assert (n > 0), 'step mush > 0'
	return fn(n-1) + fn(n-2) + fn(n-3) if n > 3 else n


if __name__ == "__main__":
	print(fn(38))
