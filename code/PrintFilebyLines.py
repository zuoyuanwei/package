# 一次性将内容读取到列表中会占用很多内存，影响执行速度。
filename = input('请输入要打开的文件：')
file = open(filename, 'r')
for line in file.readlines():   # line为文件中一行的内容，读取放入列表中，使用for in输出。
    print(line)
file.close()

# 逐行读取内容到内存中。
fliename = input('请输入要打开的文件：')
flie = open(filename, 'r')
for line in file:
    print(line)
file.close()