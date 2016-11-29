"""
用自定义格式将内存数据库对象保存到文件中；
假定数据库不使用'endrec.','enddb.'和'=>'；
假定数据库是字典的字典； 使用eval可能存在危险，它会将字符串当做代码执行；
也可以使用eval()一次创建一条字典记录；
对于print(key, file=dbfile),也可以使用dbfile.write(key + '\n');
"""

dbfilename = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'

def storeDbase(db, dbfilename=dbfilename):
	''' 将数据库格式化保存为普通文件'''
	dbfile = open(dbfilename, 'w')
	for key in db:
		# 输出到文件
		print(key, file=dbfile)
		# 遍历字典的方法，item(),数据库为字典的字典格式，即遍历的是后者字典
		for (name, value) in db[key].items():
			# repr()和str()可以使任意值转换为字符串，区别在于str()便于阅读，repr()便于解释器理解
			print(name + RECSEP + repr(value), file=dbfile)
		print(ENDREC, file=dbfile)
	print(ENDDB, file=dbfile)
	dbfile.close()

def loadDbase(dbfilename=dbfilename):
	'''
	解析数据，重新构造数据库
	'''
	dbfile = open(dbfilename)
	import sys
	sys.stdin = dbfile
	db = {}
	key = input()
	while key != ENDDB:
		rec = {}
		field = input()
		while field != ENDREC:
			name, value = field.split(RECSEP)
			rec[name] = eval(value)
			field = input()
		db[key] = rec
		key = input()
	return db

if __name__ == '__main__':
	from initdata import db
	storeDbase(db)