def getopts(argv):
	opts = {}
	while argv:
		# 找到 "-名称 值" 键值对
		if argv[0][0] == '-':
			opts[argv[0]] = argv[1]
			argv = argv[2:]
		else:
			argv = argv[1:]
	return opts

if __name__ == '__main__':
	from sys import argv
	myargs = getopts(argv)
	if '-i' in myargs:
		print(myargs['-i'])
print(myargs)

'''
收集命令行参数,并传入一个字典之中
'''
