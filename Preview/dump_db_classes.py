'''
读取shelve，打印出记录的字段
'''
import shelve
db = shelve.open('class-shelve')
for key in db:
	print(key, '=>\n', db[key].name, db[key].pay)

bob = db['bob']
print(bob.lastName())
print(db['tom'].lastName())