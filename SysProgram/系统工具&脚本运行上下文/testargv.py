import sys
print(sys.argv)
print(sys.argv[0])

'''
sys.argv输出的是一个命令行参数的列表
无论以什么方式启动,列表的第一项均为可执行脚本的名字,sys.argv[0]
'''