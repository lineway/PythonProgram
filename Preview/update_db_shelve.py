from initdata import tom
import shevle

db = shevle.open('people-shevle')
sue = db['sue']

sue['pay'] *= 1.10
db['sue'] = sue
db['tom'] = tom
db.close()