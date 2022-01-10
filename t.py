import os
file1 = open('urls.txt', 'r')
Lines = file1.readlines()
 
count = 0
for line in Lines:
    count += 1
    print("\033[32mSite{}: \033[31m{}".format(count, line.strip()))
    print("\033[37m")
    os.system("python3 dsss.py -u '{}'".format(line.strip()))
    print("\n")