import time


def logger(foo):
	def new_foo(*args, **kwars):
		start_time = time.ctime()
		result = foo(*args, **kwars)
		new_foo.__name__ = foo.__name__
		with open('logs.log', 'a', newline='\n', encoding='utf8') as write_file:
			write_file.writelines(f"Время: {start_time}, Функция: {new_foo.__name__} - {args} {kwars}, Результат:{result}\n")
		return result

	return new_foo

@logger
def myfoo(a,b):
	time.sleep(.5)
	return a * b



print(myfoo(2,5))