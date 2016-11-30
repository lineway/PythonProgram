import shelve
db = shelve.open('people-shevle')
for key in db:
	print(key, '=> \n ', db[key])
# print(db['sue']['name'])
print(db[u'sue'])
db.close()